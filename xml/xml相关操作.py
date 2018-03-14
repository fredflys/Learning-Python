#xml操作模块,内部关系明晰,效率高,推荐使用
from xml.etree import ElementTree as ET
#提供了自动缩进的xml操作模块,但功能较少,且效率低
from xml.dom import minidom
#打开本地xml文件,并读取文件内容
'''
root = ET.XML(open('xml_sample','r',encoding='utf-8').read())
print(root.tag)
for node in root:
    print(node.tag,node.attrib,node.find('year').text,node.find('rank').text)
'''

#直接解析xml文件.将文件加载到内存,可对xml进行修改
tree = ET.parse('xml_sample') #此处解析的是文件对象，不可用来解析网页xml
#获取根节点
root = tree.getroot()
#迭代找到所有节点下的year
for node in root.iter('year'):
    #读取year的值,并转换为int,进行运算
    new_year = int(node.text) + 1
    #将新的year值转回str,并重新赋值,
    node.text = str(new_year)
    #为当前结点设置新属性
    node.set('name','yeff')
    #删除当前节点的某一属性
    del node.attrib['name']

#查看root节点下提供了哪些功能
print(dir(root))
#常用的有tag,attrib,find,set,iter,get

#找到根节点下所有country节点
for country in root.findall('country'):
    #获取每个rank节点下rank节点的内容
    rank = int(country.find('rank').text)

    if rank > 60:
        #删除特定的country节点
        root.remove(country)

#这时源文件并未改变,因为这是内存中的修改.要重新写入文件
tree.write('xml_sample')


########################################################
#创建一个xml文档(从内存写入到文件中)
#创建根节点
new_xml = ET.Elemt("namelist")
#创建根节点的子节点
name1= ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age1= ET,SubElement(name1,"age",attrib={"cheked":"no"})
sex1= ET.SubElement(name1,"sex"}
sex1.text="male"
#创建根节点的子节点
name2=ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
age2=ET.SubElemet(name2,"age")
age2.texx="23"
#生成文档对象
et = ET.ElementTree(new_xml)
et.write('test.xml',encoding='utf-8',xml_declaration=True)
###################################################################
tree = ET.parse('xml_sample')
root = tree.getroot()
#创建节点
node = root.makeelement('tagname',{'attr':'value'})
#创建方法2:用类的方法生成(工厂函数)
node = ET.Element('name',{"attr":"value"})
#在很节点下添加子节点
root.append(node)
#写入文件,并避免自闭合,加上自动生成的注释
tree.write('xml_sample',short_empty_elements=False,xml_declaration=True)
#创建ElementTree对象的两个方法
tree = ET.parse(文件路径)
tree = ET._ElementTree(根节点(Element对象))
ET.element(标签名,属性) #创建一个element对象,一个element对象就是一个节点
root.append(root.makeelement()#同样在root下创建element对象
ET.SubElement(root,"name",{}))#同样在root下创建Element对象
#要写入中文,加上encoding选项
tree.write('sample',encoding='utf-8')

#####################################################
def prettify(root):
    '''将节点转为字符串,并添加缩进'''
    rough_str = ET.tostring(root,'utf-8')
    #minidom模块中的方法,将字符串面为midom中的一个类实例
    reparsed = minidom.parseString(rough_string)
    #使用类的方法,加上缩进,返回字符串
    return reparsed.toprettysml(indent='\t')
new_str = prettify(root)
with open('sample','w') as f:
    f.write(new_str)
###################################################
#命名空间
ET.register_namespace('com','http://www.company.com/')
root = ET.Element('{http://www.company.com/}')

