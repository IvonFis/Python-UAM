### Prerrequisitos

## 1. Instalacion de Anaconda

# Linux

1. Descargar el instalador de la siguiente liga:
   - https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh (64 bits)
   - https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86.sh (32 bits)

2. Ejecutar la siguiente instruccion en la terminal:
```
bash Anaconda3-5.0.1-Linux-x86_64.sh
```

3. Aceptar todos los comandos por default.

4. Cerrar y abrir una nueva terminal para que los cambios tengan efecto o reiniciar la terminal con las instrucciones:
```
cd
source .bashrc
```

5. Para probar que Anaconda se instalo correctamente, ejecutar:
```
conda list
```

# macOs

1. Descargar el instalador de la siguiente liga:
   - https://repo.continuum.io/archive/Anaconda3-5.0.1-MacOSX-x86_64.pkg

2. Ejecutar el paquete descargado.

3. Aceptar las configuraciones por default del instalador.

4. Para probar que Anaconda se instalo correctamente, ejecutar:
```
conda list
```

# Windows

1. Descargar el instalador de la siguiente liga:
   - https://repo.continuum.io/archive/Anaconda3-5.0.1-Windows-x86_64.exe
   - https://repo.continuum.io/archive/Anaconda3-5.0.1-Windows-x86.exe

2. Ejecutar el archivo descargado.

3. Aceptar las configuraciones por default del instalador.

4. Para probar que Anaconda se instalo correctamente, ejecutar:
```
conda list
```

## 2. Creacion de un Ambiente virtual

Para crear un ambiente virtial es necesario utilizar la siguiente instruccion en la temrinal:
```
conda create --name <nombre> python==<version>
```
donde <nombre> es el nombre que se desee darle al ambiente virtual y <version> es alguna version de Python. En el caso de este curso utilizaremos el nombre "UAM" y la version de Python mas reciente, la 3.6. De esta forma:
```
conda create --name UAM python==3.6
```

Una vez que se encuentre instalado el ambiente virtual es necesario activarlo, para esto:
- En Linux y macOS
  ```
  source activate UAM
  ```
- En Windows
  ```
  activate UAM
  ```

Para comprobar que el ambiente virtual fue activado es posible utilizar el comando:
```
conda env list
```
lo que debera devolver una lista de todos los ambientes virtuales en la computadora marcando el que se encuentra en uso:
```
# conda environments:
#
Tableau                  /home/enrique/anaconda2/envs/Tableau
Tableau-Python-Server     /home/enrique/anaconda2/envs/Tableau-Python-Server
UAM                   *  /home/enrique/anaconda2/envs/UAM
camera                   /home/enrique/anaconda2/envs/camera
crawlers                 /home/enrique/anaconda2/envs/crawlers
database                 /home/enrique/anaconda2/envs/database
detect                   /home/enrique/anaconda2/envs/detect
```

## 3. Instalacion de librerias para el curso

Para la instalacion de los paquetes en un ambiente virtual es necsatio activar el paquete primero:
- En Linux y macOS
  ```
  source activate UAM
  ```
- En Windows
  ```
  activate UAM
  ```

# Numpy
Libreria para el manejo de matrices y sus operaciones
```
pip install numpy
```

# Pillow
Libreria para la manipulacion de Imagenes
```
pip install pillow
```

# OpenCV
Libreria para manipulacion y segmentacion de imagenes
```
conda install opencv -c menpo
```

# Matplotlib
Libreria para crear graficas en 2D y 3D
```
pip install matplotlib
```

# Scikit-image
Libreria para manipulacion de imagenes
```
pip install scikit-image
```

# pyDicom
Libreria para la manipulacion de imagenes medicas en formato DICOM
```
pip install pydicom
```
