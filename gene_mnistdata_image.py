import sys
from tensorflow.keras.datasets import mnist
from PIL import Image
import glob

def gene_mnistdata_image(data_no,save_dir='./',speci_extension='.png'):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    image = Image.fromarray(x_train[data_no])

    file_list = glob.glob(save_dir + "*")
    print(file_list)
    save_name = 'no' + str(y_train[data_no])
    org_save_name = save_name
    save_name = save_name
    # print(save_name)
    nocnt = 0
    while save_dir + save_name + speci_extension in file_list:
        nocnt += 1
        save_name = org_save_name + "_" + str(nocnt)
        if nocnt > 10000:
            print("image numbering error")
            break
    # print(save_name)
    image.save(save_dir + save_name + speci_extension)

if __name__=="__main__":
    gene_mnistdata_image(5, './img/')