import os
import glob
import xml.etree.ElementTree as ET

image_path = os.path.join(os.getcwd(), 'images')
count = 0

for xml_file in glob.glob(image_path + '/*.xml'):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for b in root.findall('object'):
        c = b.find('name')
        if c.text.strip() == 'Field0':
            c.text = 'empty_site'
        elif c.text.strip() == 'Field1':
            c.text = 'single_tank'
        else:
            c.text = 'multiple_tank'
    count += 1
    if count%100 == 0:
        print(count)
    tree.write(xml_file)
