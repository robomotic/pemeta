#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module is to hash icons with perceptual hashing
"""

__author__ = "Paolo Di Prodi"
__copyright__ = "Copyright 2017, LogstTotal Project"
__license__ = "Apache"
__version__ = "2.0"
__maintainer__ = "Paolo Di Prodi"
__email__ = "paolo@logstotal.com"
__status__ = "Experimental"

import os
import imagehash

def hash_icons(extractor,folder_icons,mainonly = False, save=True):

    lookup = []

    groups = extractor.get_group_icons()
    if groups is None:
        return lookup
    else:
        if not os.path.exists(os.path.join(folder_icons)):
            os.makedirs(os.path.join(folder_icons))

    for group in groups:
        for i,res in enumerate(group):
            img = extractor.export(group, i)
            if img:
                img_avg_hash = imagehash.average_hash(img)
                img_dhash = imagehash.dhash(img)
                img_phash = imagehash.phash_simple(img)

                if save:
                    img.save(os.path.join(folder_icons, str(img_avg_hash) + ".ico"))

                lookup.append({'index':res.ID,
                               'average_hash':str(img_avg_hash),
                               'difference_hash':str(img_dhash),
                               'perception_phash':str(img_phash)})

                if mainonly:
                    break

        if mainonly:
            break
    return lookup

