#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the main script to extract PE icons and header information
"""

__author__ = "Paolo Di Prodi"
__copyright__ = "Copyright 2017, LogstTotal Project"
__license__ = "Apache"
__version__ = "2.0"
__maintainer__ = "Paolo Di Prodi"
__email__ = "paolo@logstotal.com"
__status__ = "Experimental"

import pefile
import argparse
import os
from extracticon import ExtractIcon
from hashicons import hash_icons
import json

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process PE file and extract information')

    parser.add_argument('--pefile',dest='filepath',type=str,required=True)

    parser.add_argument('-d','--dump_info', dest='dump_info', action='store_true')
    parser.add_argument('-i','--image_hash', dest='image_hash', action='store_true')
    parser.add_argument('-m', '--main_icon', dest='main_icon', action='store_true')
    parser.add_argument('-s', '--save_icon', dest='save_icon', action='store_true')
    parser.add_argument('-o', '--output_folder', dest='out_path', type=str)
    args = parser.parse_args()

    if args.filepath is not None:
        fileid = os.path.basename(args.filepath)
        fileid = fileid.replace(".","_")

        if args.out_path:
            os.makedirs(args.out_path, exist_ok=True)

        try:
            pe_parsed = pefile.PE(args.filepath, fast_load=True)
            pe_parsed.parse_data_directories( directories=[
                pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT'],
                pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXPORT'],
                pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_TLS'],
                pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_RESOURCE']])

            if args.image_hash:
                ico_extractor = ExtractIcon(pe_parsed)

                if args.out_path is None:
                    icons_path = os.path.join(fileid)
                    os.makedirs(icons_path, exist_ok=True)
                else:
                    icons_path = args.out_path

                icon_report = hash_icons(ico_extractor,icons_path,args.main_icon,args.save_icon)

                with open(os.path.join(icons_path,"icons.json"), "w") as rep:
                    json.dump(icon_report,rep)

            if args.dump_info:

                if args.out_path is None:
                    print(pe_parsed.dump_info())
                else:
                    summary_path = os.path.join(args.out_path,"pemeta.txt")

                    with open(summary_path,"w") as rep:
                        rep.write(pe_parsed.dump_info())

        except Exception as msg:
            raise msg

    else:
        parser.print_help()


