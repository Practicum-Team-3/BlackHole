
#############################################################################
##
## Copyright (C) 2018 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################

"""PySide2 port of the Callout example from Qt v5.x"""

import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import (QApplication, QGraphicsScene, QGraphicsView, QGraphicsSimpleTextItem, QGraphicsItem, QFrame)
from PySide2.QtCore import Qt, QPointF, QRectF, QRect, Slot, QMargins
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter, QFont, QFontMetrics, QPainterPath, QColor


class Callout(QGraphicsItem):

    def __init__(self, chart):
        QGraphicsItem.__init__(self, chart)
        self._chart = chart
        self._text = ""
        self._textRect = QRectF()
        self._anchor = QPointF()
        self._font = QFont()
        self._rect = QRectF()

    # returns an estimate of the area painted by the item
    def boundingRect(self):
        anchor = self.mapFromParent(self._chart.mapToPosition(self._anchor))
        # rect to be returned
        rect = QRectF()
        rect.setLeft(min(self._rect.left(), anchor.x()))
        rect.setRight(max(self._rect.right(), anchor.x()))
        rect.setTop(min(self._rect.top(), anchor.y()))
        rect.setBottom(max(self._rect.bottom(), anchor.y()))

        return rect

    # implements the actual painting
    def paint(self, painter, option, widget):
        path = QPainterPath()
        path.addRoundedRect(self._rect, 5, 5)
        anchor = self.mapFromParent(self._chart.mapToPosition(self._anchor))
        if not self._rect.contains(anchor) and not self._anchor.isNull():
            point1 = QPointF()
            point2 = QPointF()

            # establish the position of the anchor point in relation to _rect
            above = anchor.y() <= self._rect.top()
            aboveCenter = (anchor.y() > self._rect.top() and
                anchor.y() <= self._rect.center().y())
            belowCenter = (anchor.y() > self._rect.center().y() and
                anchor.y() <= self._rect.bottom())
            below = anchor.y() > self._rect.bottom()

            onLeft = anchor.x() <= self._rect.left()
            leftOfCenter = (anchor.x() > self._rect.left() and
                anchor.x() <= self._rect.center().x())
            rightOfCenter = (anchor.x() > self._rect.center().x() and
                anchor.x() <= self._rect.right())
            onRight = anchor.x() > self._rect.right()

            # get the nearest _rect corner.
            x = (onRight + rightOfCenter) * self._rect.width()
            y = (below + belowCenter) * self._rect.height()
            cornerCase = ((above and onLeft) or (above and onRight) or
                (below and onLeft) or (below and onRight))
            vertical = abs(anchor.x() - x) > abs(anchor.y() - y)

            x1 = (x + leftOfCenter * 10 - rightOfCenter * 20 + cornerCase *
                int(not vertical) * (onLeft * 10 - onRight * 20))
            y1 = (y + aboveCenter * 10 - belowCenter * 20 + cornerCase *
                vertical * (above * 10 - below * 20))
            point1.setX(x1)
            point1.setY(y1)

            x2 = (x + leftOfCenter * 20 - rightOfCenter * 10 + cornerCase *
                int(not vertical) * (onLeft * 20 - onRight * 10))
            y2 = (y + aboveCenter * 20 - belowCenter * 10 + cornerCase *
                vertical * (above * 20 - below * 10))
            point2.setX(x2)
            point2.setY(y2)

            path.moveTo(point1)
            path.lineTo(anchor)
            path.lineTo(point2)
            path = path.simplified()

        painter.setBrush(QColor(255, 255, 255))
        painter.drawPath(path)
        painter.drawText(self._textRect, self._text)

    def mousePressEvent(self, event):
        event.setAccepted(True)

    def mouseMoveEvent(self, event):
        # check for left button
        if event.buttons() & Qt.LeftButton:
            # change origin of item (self)
            self.setPos(self.mapToParent(event.pos() - event.buttonDownPos(Qt.LeftButton)))
            event.setAccepted(True)
        else:
            event.setAccepted(False)

    # set text of an item and center it?
    def setText(self, text):
        self._text = text
        metrics = QFontMetrics(self._font)
        self._textRect = QRectF(metrics.boundingRect(QRect(0.0, 0.0, 150.0, 150.0),Qt.AlignLeft, self._text))
        self._textRect.translate(5, 5)
        self.prepareGeometryChange()
        self._rect = self._textRect.adjusted(-5, -5, 5, 5)

    # helper function to set the anchor of an item
    def setAnchor(self, point):
        self._anchor = QPointF(point)

    # helper function to change the position of an item to reflect the anchor
    def updateGeometry(self):
        self.prepareGeometryChange()
        self.setPos(self._chart.mapToPosition(self._anchor) + QPointF(10, -50))


class NetworkGraph(QGraphicsView):

    def __init__(self, parent = None):
        super(NetworkGraph, self).__init__(parent)
        self.setScene(QGraphicsScene(self))


        self.setDragMode(QGraphicsView.NoDrag)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        #self.setFrameShape(QFrame.NoFrame)

        # Chart
        self._chart = QtCharts.QChart()
        self._chart.setBackgroundRoundness(0)
        self._chart.setMargins(QMargins(-28, -9, -11, -23)) # make sure the graphing area fills the whole chart view
        # self._chart.zoom(0.1)
        self._chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self._chart.setTheme(QtCharts.QChart.ChartThemeDark)
        #self._chart.setMinimumSize(340, 280)
        #self._chart.setTitle("Hover the line to show callout. Click the line to make it stay")
        self._chart.legend().hide()

        # Series 1
        self.series = QtCharts.QLineSeries()
        self.series.append(1, 3)
        self.series.append(4, 5)
        self.series.append(6, 2)
        self._chart.addSeries(self.series)

        # Series 2
        self.series2 = QtCharts.QLineSeries()
        self.series2.append(4, 5)
        self.series2.append(5, 6)
        self._chart.addSeries(self.series2)

        # Scatter
        self.seriesS = QtCharts.QScatterSeries()
        self.seriesS.setMarkerShape(QtCharts.QScatterSeries.MarkerShapeCircle)
        self.seriesS.append(1, 3)
        self.seriesS.append(4, 5)
        self.seriesS.append(5, 6)
        self.seriesS.append(6, 2)
        self._chart.addSeries(self.seriesS)

        # Create axes and config grid invisible
        self._chart.createDefaultAxes()
        self.axes = self._chart.axes()
        for axis in self.axes:
            axis.setLabelsVisible(False)
            axis.setGridLineVisible(False)
            axis.setLineVisible(False)
        self._chart.setAcceptHoverEvents(True)

        # Add to scene
        self.setRenderHint(QPainter.Antialiasing)
        self.scene().addItem(self._chart)

        # Callout setup
        self._callouts = []
        self._tooltip = Callout(self._chart)

        self.series.clicked.connect(self.keepCallout)
        self.series.hovered.connect(self.tooltip)

        self.series2.clicked.connect(self.keepCallout)
        self.series2.hovered.connect(self.tooltip)

        self.setMouseTracking(True)


    def resizeEvent(self, event):
        super().resizeEvent(event)

        size = event.size()
        size = size.grownBy(QMargins(12, 12, 12, 12))
        if self.scene():
            self.scene().setSceneRect(QRectF(QPointF(12, 12), size))
            self._chart.resize(size)

            for callout in self._callouts:
                callout.updateGeometry()
        #QGraphicsView.resizeEvent(self, event)

    # What was dis for?
    #def mouseMoveEvent(self, event):

        #QGraphicsView.mouseMoveEvent(self, event)

    # Called by clicking series, will keep the callout on screen
    def keepCallout(self):
        # place the callout that we're keeping with the others that we kept
        self._callouts.append(self._tooltip)
        # init a new callout for the future
        self._tooltip = Callout(self._chart)

    # Called by hovering event on series
    def tooltip(self, point, state):

        if self._tooltip == 0: # Need to init a new Callout and place on _tooltip
            self._tooltip = Callout(self._chart)

        # mouse is over
        if state:
            self._tooltip.setText("X: {0:.2f} \nY: {1:.2f} ".format(point.x(),point.y()))
            self._tooltip.setAnchor(point)
            self._tooltip.setZValue(11)
            self._tooltip.updateGeometry()
            self._tooltip.show()
        # mouse out
        else:
            self._tooltip.hide()

