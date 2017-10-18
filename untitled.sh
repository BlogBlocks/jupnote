#!/bin/bash
#
# Script for generating spatial resolution test images
# Made by Antti Lipponen (Twitter @anttilip)
#
#
# Imagemagick and gdal used for processing
#
#
# Test cases:
#
#     San Francisco, 21 Dec 2016
#     http://sentinel-s2-l1c.s3-website.eu-central-1.amazonaws.com/#tiles/10/S/EG/2016/12/21/0/
#
#     Center-pivot irrigation in Sahara, 6 Feb 2017
#     http://sentinel-s2-l1c.s3-website.eu-central-1.amazonaws.com/#tiles/35/R/PK/2017/2/6/0/ 
#
#     Brahmaputra river, 19 Jan 2017
#     http://sentinel-s2-l1c.s3-website.eu-central-1.amazonaws.com/#tiles/46/R/EQ/2017/1/19/0/
#
#     Lake Pukaki, 27 Jan 2017
#     http://sentinel-s2-l1c.s3-website.eu-central-1.amazonaws.com/#tiles/59/G/MM/2017/1/27/0/

# Download Sentinel files
if [ ! -f TCI_SanFrancisco.jp2 ]; then
	wget -O TCI_SanFrancisco.jp2 http://sentinel-s2-l1c.s3.amazonaws.com/tiles/10/S/EG/2016/12/21/0/TCI.jp2
fi

if [ ! -f TCI_Sahara.jp2 ]; then
	wget -O TCI_Sahara.jp2 http://sentinel-s2-l1c.s3.amazonaws.com/tiles/35/R/PK/2017/2/6/0/TCI.jp2
fi

if [ ! -f TCI_Brahmaputra.jp2 ]; then
	wget -O TCI_Brahmaputra.jp2 http://sentinel-s2-l1c.s3.amazonaws.com/tiles/46/R/EQ/2017/1/19/0/TCI.jp2
fi

if [ ! -f TCI_Pukaki.jp2 ]; then
	wget -O TCI_Pukaki.jp2 http://sentinel-s2-l1c.s3.amazonaws.com/tiles/59/G/MM/2017/1/27/0/TCI.jp2
fi

for RESOLUTION in 10 15 20 30 60 100 120 250
do
	# San Francisco
	gdalwarp -t_srs '+proj=utm +zone=10 +datum=WGS84' -of GTiff -te 549000 4180000 557000 4188000 -tr $RESOLUTION $RESOLUTION -r cubic TCI_SanFrancisco.jp2 tmpoutput.tif
	convert tmpoutput.tif -resize 800x800 -unsharp 5x2+1+0 -sampling-factor 4:2:2 -quality 95 SanFrancisco_${RESOLUTION}m.jpg
	rm tmpoutput.tif

	# Sahara
	gdalwarp -t_srs '+proj=utm +zone=35 +datum=WGS84' -of GTiff -te 612000 2985000 620000 2993000 -tr $RESOLUTION $RESOLUTION -r cubic TCI_Sahara.jp2 tmpoutput.tif
	convert tmpoutput.tif -resize 800x800 -unsharp 5x2+1+0 -sampling-factor 4:2:2 -quality 95 Sahara_${RESOLUTION}m.jpg
	rm tmpoutput.tif

	# Brahmaputra
	gdalwarp -t_srs '+proj=utm +zone=46 +datum=WGS84' -of GTiff -te 582912 2963445 590912 2971445 -tr $RESOLUTION $RESOLUTION -r cubic TCI_Brahmaputra.jp2 tmpoutput.tif
	convert tmpoutput.tif -resize 800x800 -unsharp 5x2+1+0 -sampling-factor 4:2:2 -quality 95 Brahmaputra_${RESOLUTION}m.jpg
	rm tmpoutput.tif

	# Pukaki
	gdalwarp -t_srs '+proj=utm +zone=59 +south +datum=WGS84' -of GTiff -te 428498 5135275 436498 5143275 -tr $RESOLUTION $RESOLUTION -r cubic TCI_Pukaki.jp2 tmpoutput.tif
	convert tmpoutput.tif -resize 800x800 -unsharp 5x2+1+0 -sampling-factor 4:2:2 -quality 95 Pukaki_${RESOLUTION}m.jpg
	rm tmpoutput.tif
done