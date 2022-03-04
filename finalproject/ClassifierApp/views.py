from django.shortcuts import render
from .forms import EntryForm
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
# Список категорий из CIFAR10
classes = ["airplane", "automobile", "bird", "cat",
           "deer", "dog", "frog", "horse", "ship", "truck"]


# Prediction для определенния картинки
def prediction(path):
    # Загружаем нашу модель
    model = load_model("myNewModel.h5")
    # Загружаем изображение и меням размер
    myimage = image.load_img(path, target_size=(32, 32))
    # Превращаем его в array
    myimage = image.img_to_array(myimage)
    # Меням каналы
    myimage = myimage.reshape(1, 32, 32, 3)
    # preparing pixel data
    myimage = myimage.astype('float32')
    myimage = myimage / 255.0
    # Predicting wiht model
    predictions = model.predict(myimage)
    # Вывод самого вероятного результата
    return classes[np.argmax(predictions, axis=1)[0]]

# Rendering view
def main_view(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.instance
            img.save()
            img.title = prediction(img.image.path)
            img.save()
            return render(request, 'index.html', {'form': form, 'img': img})
    else:
        form = EntryForm()
    return render(request, 'index.html', {'form': form})
