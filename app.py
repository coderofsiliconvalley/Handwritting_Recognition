import network
import collect
import showImage


training_data, validation_data, test_data , training_data_orig = collect.load_data()

print("len training data:",len(training_data[0]))

images = showImage.get_images(training_data_orig) 

# showImage.plot_images_together(images)
showImage.plot_box_images(images)
showImage.plotDigit(images[0])


net = network.NeuralNetwork([784, 30, 10])
net.fit(training_data, validation_data)

