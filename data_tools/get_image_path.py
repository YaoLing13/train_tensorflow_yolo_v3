import os
import sys
import argparse

def main(dir_path_of_anno, save_dir, save_name):
    # line = [f for f in os.listdir(dir_path_of_anno) if os.path.isfile(os.path.join(dir_path_of_anno, f))]
    f = os.listdir(dir_path_of_anno)
    save_file = save_dir + '/' + save_name
    txt_file = open(save_file, 'w')
    for name in f:
        file_name = dir_path_of_anno+'/'+name+'\n'
        txt_file.write(file_name)
    txt_file.close()
    print('Done!')


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--dir_path_of_anno", default="", help="The directory path which file exits")
    args.add_argument("--save_dir", default="./", help="The directory path which save")
    args.add_argument("--save_name", default="train_annotation.txt", help="The file name which would generate")
    FLAGS = args.parse_args()

    if len(FLAGS.dir_path_of_anno) == 0:
        print("Please Input 'dir_path_of_anno' !")
        exit()
    main(FLAGS.dir_path_of_anno, FLAGS.save_dir, FLAGS.save_name)