import xml.etree.ElementTree as ET

class KNX():
    def __init__(self,MT='MT',TV='5.1.255.16695'):
        self.CreatedBy=MT
        self.ToolVersion=TV
        self.ManufacturerData

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print("{:s} Created by: {:s}, Tool Version: {:s}".format(self.CreatedBy, self.ToolVersion))

class ManufacturerData():
    def __init__(self):
        self.Manufacturer

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print("  ",self.getName())

class Manufacturer():
    def __init__(self, RefId='M-0083'):
        self.RefId=RefId
        self.ApplicationPrograms

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print("{:s} RefId {:s}".format(self.getName(),self.RefId))

class ApplicationPrograms():
    def __init__(self):
        self.ApplicationProgram

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print("", self.getName())

class ApplicationProgram():
    def __init__(self,Id= 'M-0083_A-008A-13-D647', ApplicationNumber = '138', ApplicationVersion= '19',
                 ProgramType = 'ApplicationProgram', MaskVersion = 'MV-0705', Name = 'Push Button II Smart, Temperature',
                 LoadProcedureStyle = 'ProductProcedure', PeiType ='1', HelpFile = '', DefaultLanguage= 'en-US',
                 DynamicTableManagement= 'false', Linkable= 'false', MinEtsVersion= '4.0', CreatedFromLegacySchemaVersion = 'true',
                 ReplacesVersions= '16 17 18', Hash= '1qwqREZD8Axy1D+GEbFURw=='):
        self.Id=Id
        self.ApplicationNumber=ApplicationNumber
        self.ApplicationVersion=ApplicationVersion
        self.ProgramType=ProgramType
        self.MaskVersion=MaskVersion
        self.Name=Name
        self.LoadProcedureStyle=LoadProcedureStyle
        self.PeiType=PeiType
        self.HelpFile=HelpFile
        self.DefaultLanguage=DefaultLanguage
        self.DynamicTableManagement=DynamicTableManagement
        self.Linkable=Linkable
        self.MinEtsVersion=MinEtsVersion
        self.CreatedFromLegacySchemaVersion=CreatedFromLegacySchemaVersion
        self.ReplacesVersions=ReplacesVersions
        self.Hash=Hash
        self.Static

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(" ",self.getName(), Id,ApplicationNumber,ApplicationVersion,ProgramType,MaskVersion,Name,LoadProcedureStyle,PeiType,HelpFile,DefaultLanguage,DynamicTableManagement,Linkable,MinEtsVersion,CreatedFromLegacySchemaVersion,ReplacesVersions,Hash)

class Static():
    def __init__(self):
        self.Code
        self.ParameterTypes
        self.Parameters
        self.ParameterRefs
        self.ComObjectTable
        self.ComObjectRefs
        self.AddressTable
        self.AssociationTable
        self.LoadProcedures

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class Code():
    def __init__(self):
        self.AbsoluteSegment=[]

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class AbsoluteSegment():
    def __init__(self,Id= '', MemoryType= '', Address= '', Size= ''):
        self.Id = Id
        self.MemoryType = MemoryType
        self.Address = Address
        self.Size = Size
        self.Data
        self.Mask

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),Id, MemoryType, Address, Size)

class Data():
    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class Mask():
    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class ParameterTypes():
    def __init__(self):
        self.ParameterType=[]

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class ParameterType():
    def __init__(self,Id = '', Name= ''):
        self.Id=Id
        self.Name=Name
        self.TypeNumber
        self.TypeRestriction
        self.TypeText
        self.TypeFloat
        self.TypePicture

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),Id , Name)

class TypeNumber():
    def __init__(self,SizeInBit ='', Type='', minInclusive= '', maxInclusive= ''):
        self.SizeInBit=SizeInBit
        self.Type=Type
        self.minInclusive=minInclusive
        self.maxInclusive=maxInclusive

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),SizeInBit, Type, minInclusive, maxInclusive)

class TypeRestriction():
    def __init__(self,Base='', SizeInBit=''):
        self.SizeInBit=SizeInBit
        self.Base=Base
        self.Enumeration=[]

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),Base, SizeInBit)

class Enumeration():
    def __init__(self,Text='', Value='', Id=''):
        self.Text=Text
        self.Value=Value
        self.Id=Id

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),Text, Value, Id)

class TypeText():
    def __init__(self,SizeInBit='', Pattern=''):
        self.SizeInBit=SizeInBit
        self.Pattern=Pattern

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),SizeInBit, Pattern)

class TypeFloat():
    def __init__(self,Encoding='', minInclusive='', maxInclusive=''):
        self.Encoding=Encoding
        self.minInclusive=minInclusive
        self.maxInclusive=maxInclusive

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),Encoding, minInclusive, maxInclusive)

class TypePicture():
    def __init__(self,RefId=''):
        self.RefId=RefId

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),RefId)

class Parameters():
    def __init__(self):
        self.Parameter=[]
        self.Union=[]

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class Parameter():
    def __init__(self,Id='', Name='', ParameterType='', Text='', Value=''):
        self.Id=Id
        self.Name=Name
        self.ParameterType=ParameterType
        self.Text=Text
        self.Value=Value
        self.Memory

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),Id, Name, ParameterType, Text, Value)

class Union():
    def __init__(self,SizeInBit=''):
        self.SizeInBit=SizeInBit
        self.Memory

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),SizeInBit)

class Memory():
    def __init__(self,CodeSegment='', Offset='', BitOffset=''):
        self.CodeSegment=CodeSegment
        self.Offset=Offset
        self. BitOffset= BitOffset

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),CodeSegment, Offset, BitOffset)

class ParameterRefs():
    def __init__(self):
        self.ParameterRef=[]

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class ParameterRef():
    def __init__(self,Id='', RefId='', Text='', Tag='',Access = '',Value=''):
        self.Id=Id
        self.RefId=RefId
        self.Text=Text
        self.Tag=Tag
        self.Access=Access
        self.Value=Value

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),Id, RefId, Text, Tag,Access ,Value)

class ComObjectTable():
    def __init__(self):
        self.ComObject=[]

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class ComObject():
    def __init__(self,Id='', Name='', Text='', Number='', FunctionText='', ObjectSize='', ReadFlag='', WriteFlag='', CommunicationFlag='', TransmitFlag='', UpdateFlag='', ReadOnInitFlag='', DatapointType=''):
        self.Id=Id
        self.Name=Name
        self.Text=Text
        self.Number=Number
        self.FunctionText=FunctionText
        self.ObjectSize=ObjectSize
        self.ReadFlag=ReadFlag
        self.WriteFlag=WriteFlag
        self.CommunicationFlag=CommunicationFlag
        self.TransmitFlag=TransmitFlag
        self.UpdateFlag=UpdateFlag
        self.ReadOnInitFlag=ReadOnInitFlag
        self.DatapointType=DatapointType


    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),Id, Name, Text, Number, FunctionText, ObjectSize, ReadFlag, WriteFlag, CommunicationFlag, TransmitFlag, UpdateFlag, ReadOnInitFlag, DatapointType)

class ComObjectRefs():
    def __init__(self):
        self.ComObjectRef=[]

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class ComObjectRef():
    def __init__(self,Id='', RefId='', Text='', Tag='', FunctionText='', ObjectSize='', ReadFlag='', WriteFlag='',CommunicationFlag='',TransmitFlag='', UpdateFlag='', DatapointType=''):
        self.Id=Id
        self.RefId=RefId
        self.Text=Text
        self.Tag=Tag
        self.FunctionText=FunctionText
        self.ObjectSize=ObjectSize
        self.ReadFlag=ReadFlag
        self.WriteFlag=WriteFlag
        self.CommunicationFlag=CommunicationFlag
        self.TransmitFlag=TransmitFlag
        self.UpdateFlag=UpdateFlag
        self.DatapointType=DatapointType

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),Id, RefId, Text, Tag, FunctionText, ObjectSize, ReadFlag, WriteFlag, CommunicationFlag, TransmitFlag, UpdateFlag, DatapointType)

class AddressTable():
    def __init__(self,CodeSegment='', Offset='', MaxEntries=''):
        self.CodeSegment=CodeSegment
        self.Offset=Offset
        self.MaxEntries=MaxEntries

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),CodeSegment, Offset, MaxEntries)

class AssociationTable():
    def __init__(self,CodeSegment='', Offset='', MaxEntries=''):
        self.CodeSegment=CodeSegment
        self.Offset=Offset
        self.MaxEntries=MaxEntries

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),CodeSegment, Offset, MaxEntries)

class LoadProcedures():
    def __init__(self):
        self.LoadProcedure

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class LoadProcedure():
    def __init__(self):
        self.LdCtrlConnect
        self.LdCtrlCompareProp
        self.LdCtrlUnload=[]
        self.LdCtrlLoad=[]
        self.LdCtrlAbsSegment=[]
        self.LdCtrlTaskSegment=[]
        self.LdCtrlLoadCompleted=[]
        self.LdCtrlRestart
        self.LdCtrlDisconnect

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class LdCtrlConnect():
    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class LdCtrlRestart():
    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class LdCtrlDisconnect():
    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class LdCtrlUnload():
    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName())

class LdCtrlCompareProp():
    def __init__(self,ObjIdx='', PropId='', InlineData=''):
        self.ObjIdx=ObjIdx
        self.PropId=PropId
        self.InlineData=InlineData

    def getName(self):
        return self.__class__.__name__

    def Print(self):
        print(self.getName(),ObjIdx='', PropId='', InlineData)
