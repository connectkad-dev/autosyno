# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AutoSyno
                                 A QGIS plugin
 Auto'Syno vous permet de générer le syno de votre projet en toute simplicité!

                             -------------------
        begin                : 2020-02-10
        copyright            : (C) 2020 by EDS for METIS RESEAUX
        email                : n.rosa@metis-reseaux.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    from .autosyno import AutoSyno
    return AutoSyno(iface)
