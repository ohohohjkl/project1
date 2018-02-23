import xml.etree.ElementTree as ET

tree = ET.parse('M-0083_A-008A-13-D647.xml')

root = tree.getroot()
#
# # for element in root:
# #      print ('parent: ', element.tag, '|', element.attrib)
# #      print (element.text)
# #      for all_tags in element.findall('.//'):
# #          print ('child: ', all_tags.tag, '|', all_tags.attrib)
# #          if all_tags.text:
# #              print (all_tags.text, '|', all_tags.tail)
#
# # print(root.tag,root.attrib)
# # i=0
#
# print("Nhap ETS Text: ")
# s = input()
#
# for child in root.iter():
#     if (
#             child.tag == "{http://knx.org/xml/project/11}Translation" or child.tag == "{http://knx.org/xml/project/11}TranslationElement"
#             or child.tag == "{http://knx.org/xml/project/11}choose"
#             or child.tag == "{http://knx.org/xml/project/11}when"
#             or child.tag == "{http://knx.org/xml/project/11}ParameterRefRef"):
#         continue
#     text = child.get("Text")
#     funcText = child.get("FunctionText")
#     # ID=child.get("ID")
#     if (s == text or s == funcText):
#         if(child.get("Id")):
#             ID = child.get("Id")
#         else:
#             ID= child.get("RefId")
#         print(child.tag, child.attrib)
#         for child2 in root.iter():
#             if (ID == child2.get("ID") or ID == child2.get("RefId")):
#                 print(child2.tag, child2.attrib)
#         s1 = input()
#
# # for child in root.findall(".//*[@ParameterType]"):
# #     print(child.tag, child.attrib)


# for element in root:
#      print ('parent: ', element.tag, '|', element.attrib)
#      print (element.text)
#      for all_tags in element.findall('.//'):
#          print ('child: ', all_tags.tag, '|', all_tags.attrib)
#          if all_tags.text:
#              print (all_tags.text, '|', all_tags.tail)

# print(root.tag,root.attrib)
# i=0

# print("Nhap ETS Text: ")
# s = input()
#
# for child in root.iter():
#     if (
#             child.tag == "{http://knx.org/xml/project/11}Translation" or child.tag == "{http://knx.org/xml/project/11}TranslationElement"
#             or child.tag == "{http://knx.org/xml/project/11}choose"
#             or child.tag == "{http://knx.org/xml/project/11}when"
#             or child.tag == "{http://knx.org/xml/project/11}ParameterRefRef"):
#         continue
#     text = child.get("Text")
#     funcText = child.get("FunctionText")
#     # ID=child.get("ID")
#     if (s == text or s == funcText):
#         if(child.get("Id")):
#             ID = child.get("Id")
#         else:
#             ID= child.get("RefId")
#         print(child.tag, child.attrib)
#         for child2 in root.iter():
#             if (ID == child2.get("ID") or ID == child2.get("RefId")):
#                 print(child2.tag, child2.attrib)
#         s1 = input()

# for child in root.findall(".//*[@ParameterType]"):
#     print(child.tag, child.attrib)

##########################LK tag####################
dem = 0
dem2 = 0

# for child in root.iter():
#     print(" PARENT:  ", child.tag,child.attrib)
#     for child2 in child.findall("*"):
#         print(" CHILD:")
#         print(child2.tag,child2.attrib)
#         dem=dem+1
#         dem2=dem2+1
#         print("Number of child: ", dem)
#     #     if(dem2==200):
#     #         s1=input()
#     #         dem2 = 0
#     # dem=
#     s1=input()
#####################################################


########### {http://knx.org/xml/project/11}
while True:
    s = "{http://knx.org/xml/project/11}"
    print("Nhap tag:")
    s = s + input()
    for child in root.iter(s):
        print(child.tag, child.attrib)

# print(root.tag)
# for child in root.iter():
#     for child2 in child.findall("*"):
#         print(" CHILD:")
#         print(child2.tag)
#         dem=dem+1
#         print("Number of child: ", dem)
#     dem=0


