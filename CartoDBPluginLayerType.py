"""
/***************************************************************************
CartoDB Plugin
A QGIS plugin

----------------------------------------------------------------------------
begin                : 2014-09-08
copyright            : (C) 2014 by Michael Salgado, Kudos Ltda.
email                : michaelsalgado@gkudos.com, info@gkudos.com
***************************************************************************/

/***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************/
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from CartoDBPluginLayer import CartoDBPluginLayer


class CartoDBPluginLayerType(QgsPluginLayerType):

    def __init__(self):
        QgsPluginLayerType.__init__(self, CartoDBPluginLayer.LAYER_TYPE)

    def createLayer(self):
        return CartoDBPluginLayer()

    def showLayerProperties(self, layer):
        return True
