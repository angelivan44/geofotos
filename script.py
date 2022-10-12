from PIL import Image
import simplekml
import os

def filter_files(arg):
    data = arg.split(".")[-1]
    if data == "jpg":
        return data
        
    

def script_main(image_path, save_dir):
    
    print(image_path)
    documents = os.listdir(image_path)
    filter_documents = list(filter(filter_files, documents))
    print(documents, filter_documents)
    kml = simplekml.Kml()
    folder = kml.newfolder(name="Fotos")
    file = """file:///"""
    for index, picture in enumerate(filter_documents):
        path = image_path + "\\" + picture
        try:
            image = Image.open(path)
            metada = image._getexif()
        except:
            image = None
            metada = {}
        try:
            ubication = metada[34853]
        except:
            ubication = "none"
        
        def DMS2DD(data, direction):
                dd = float(float(data[0]) + float(data[1]/60) + float(data[2]/3600));
                if (direction == "S" or direction == "W") :
                    dd = dd * -1; 
                return dd
        if(ubication != "none"):
            norte = DMS2DD(ubication[2],ubication[1])
            este = DMS2DD(ubication[4],ubication[3])
        
            descripcion =  f"""<html> 
                                                <div style="width: 550px;height: 600px;"><h3 style="font-size:22px;color:white;background-color: red;text-align: center;">Foto</h3>
                                                <table style="border:1px solid black;width: 550px;height: 600px; cellspacing:0;" >
                                                    <tr>
                                                    <td style="border:1px solid">
                                                            <img style="width:550; height:420; border:1; bordercolor:blue; transform: rotate(90deg); -webkit-transform: rotate(90deg);" src="{file}{path}">
                                                    </td>
                                                    </tr>
                                                </table >
                                                </div>
                                                </html>
                                                    """
            folder.newpoint(name=str(index), coords=[(este,norte)], description=descripcion)
    kml.save(path=str(save_dir + "\\" + "exportacion.kml"), format=True)
    return True