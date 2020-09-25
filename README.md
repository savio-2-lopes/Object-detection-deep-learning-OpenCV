<h2 align="center">
    <b>Detectação de objetos com deep learning e OpenCV</b> 
</h2>

<br> 

# Índice

- [Sobre](#sobre)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Usar](#como-usar)

<a id="sobre"></a>

## :bookmark: Sobre

Esta aplicação é uma forma de realizar a detecção de objetos utilizando MobileNets + SSD juntamente com OpenCV e o módulo dnn, para detectar objetos em imagens.
<br>
Essa aplicação foi baseada no artigo do blog [Pyimagesearch](https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/)

<br> 

<a id="tecnologias-utilizadas"></a>

## :rocket: Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias

- [TensorFlow](https://www.tensorflow.org/lite/models/object_detection/overview)
- [Pyhon](https://www.python.org/)
- [OpenCV](https://www.python.org/)

<br> 

## :fire: Como usar


```sh

# Para testar a aplicação rode o comando:

$ python object_detection.py \
	--prototxt MobileNetSSD_deploy.prototxt.txt \
	--model MobileNetSSD_deploy.caffemodel --image exemplo/exemplo_01.jpg 
	
# O resultado será a verificação do conteúdo da imagem escolhida dentro do diretório exemplo (a imagem em questão é exemplo_01.jpg)

```

