# Author: Felix Fischer
# Transforms a ASCII Point cloud into 3 files. One 16 bit .png containing the color values, and two 8 bit .png files containing the xyz coordinates.
import glob
import ntpath
import os

from PIL import Image

from .classes import Logger

log = Logger("PointCloud2Map")


def gen_filennames(protein):
    pass
    # protein = protein.split("/")[-1].rstrip(".ply")
    # if current_workdir is None:
    #     current_workdir = os.getcwd()
    #     f = open(current_workdir + "/ASCII_clouds/" + protein + ".xyzrgb", "r")
    # else:
    #     f = open(file, "r")
    #     protein = protein.split("/")[-1].rstrip(".xyzrgb")


def pcd_to_png(ascii_file, rgb_file, xyz_low_file, xyz_high_file, img_size=512):

    # xyzrgb file comes with RGB stores as float. RGB values between 0.0 and 1.0 and XYZ values between -x and x -> TODO: Range?
    f = open(ascii_file, "r")

    log.debug(f"Image size is: {img_size}x{img_size}")
    x, y, z = [], [], []

    n1_X = []
    n1_Y = []
    n1_Z = []

    n2_X = []
    n2_Y = []
    n2_Z = []
    n = [[n1_X, n1_Y, n1_Z], [n2_X, n2_Y, n2_Z]]
    R = []
    G = []
    B = []

    lines = list(f.readlines())

    log.debug(f"source is {ascii_file}")

    for i in range(img_size * img_size):
        # print(i)
        if i >= len(lines):
            # add zeros
            x.append(0)
            y.append(0)
            z.append(0)

            R.append(0)
            G.append(0)
            B.append(0)

        else:
            line = lines[i]
            new_line = list(line.strip().split(" "))

            #!
            #!convert float RGB values [0,1] to [0,255] = int values of RGB
            #!
            try:
                new_line[3] = float(new_line[3]) * 255  # type: ignore
                new_line[4] = float(new_line[4]) * 255  # type: ignore
                new_line[5] = float(new_line[5]) * 255  # type: ignore
            except IndexError as e:
                log.debug(f"{i},{new_line}")
                raise IndexError(e)
            if len(new_line) >= 3:
                # Extract xyz values
                p_x = float(new_line[0])
                p_y = float(new_line[1])
                p_z = float(new_line[2])
                # Transform them to a float and separate them into 2 8bit arrays
                x.append(float(p_x))
                y.append(float(p_y))
                z.append(float(p_z))

            if len(new_line) >= 6:
                # extract rgb values
                r = new_line[3]
                g = new_line[4]
                b = new_line[5]
                # transform them to float and than to int
                R.append(int(float(r)))  # TODO: Do we need that? *180 makes it brighter
                G.append(int(float(g)))
                B.append(int(float(b)))
            else:
                R.append(0)
                G.append(0)
                B.append(0)

    f.close()

    # Transform coordinates to the positive space
    ###########################################
    max_x = max(x)
    min_x = min(x)

    max_y = max(y)
    min_y = min(y)

    max_z = max(z)
    min_z = min(z)

    # print(max_x-min_x,max_y-min_y,max_z-min_z)
    for k in range(len(x)):

        xn = int(float((x[k] - min_x) / (max_x - min_x)) * 65535)  # 65535
        yn = int(float((y[k] - min_y) / (max_y - min_y)) * 65535)
        zn = int(float((z[k] - min_z) / (max_z - min_z)) * 65535)
        # f.write('%s,%s,%s,%.6f,%.6f,%.6f,%s\n' %(n,n,n,xn,yn,l_z[n],l_rest[n]))
        # if k == 500:
        #     print(xn, yn, zn)
        #     exit()
        sx = xn % 255
        sy = yn % 255
        sz = zn % 255

        ex = xn // 255
        ey = yn // 255
        ez = zn // 255

        n1_X.append(sx)
        n1_Y.append(sy)
        n1_Z.append(sz)

        n2_X.append(ex)
        n2_Y.append(ey)
        n2_Z.append(ez)

    # f.write('%s,%s,%s,'%(xn,yn,zn))
    # f.close()
    # Fill arrays with xyz(8bit) / rgb(16bit) values
    ####################################
    coordsarray_1 = [(0, 0, 0)] * img_size * img_size
    coordsarray_2 = coordsarray_1.copy()
    colarray = coordsarray_1.copy()

    for i in range(0, img_size * img_size):
        coordsarray_1[i] = (n1_X[i], n1_Y[i], n1_Z[i])
        coordsarray_2[i] = (n2_X[i], n2_Y[i], n2_Z[i])
        colarray[i] = (R[i], G[i], B[i])

    # Output the files
    #################################
    # Define output paths and create directory if needed
    # output_path_rgb = current_workdir + "/MAPS/rgb/"
    # output_path_xyz_high = current_workdir + "/MAPS/xyz/high/"
    # output_path_xyz_low = current_workdir + "/MAPS/xyz/low/"
    # rgb_file = f"{output_path_rgb}{protein}.png"
    # xyz_high_file = f"{output_path_xyz_high}{protein}.bmp"
    # xyz_low_file = f"{output_path_xyz_low }{protein}.bmp"
    # if not os.path.exists(output_path_rgb):
    #     os.makedirs(output_path_rgb)
    # if not os.path.exists(output_path_xyz_high):
    #     os.makedirs(output_path_xyz_high)
    # if not os.path.exists(output_path_xyz_low):
    #     os.makedirs(output_path_xyz_low)

    # Write RGB values to png file
    imagec = Image.new("RGB", (img_size, img_size))
    imagec.putdata(colarray)  # type: ignore
    save_location, _ = ntpath.split(rgb_file)
    os.makedirs(save_location, exist_ok=True)
    imagec.save(rgb_file)
    log.debug(f"RGB map saved to {rgb_file}")

    # Write XYZ values to bmp files
    imagel = Image.new("RGB", (img_size, img_size))
    imagel.putdata(coordsarray_1)  # type: ignore
    save_location, _ = ntpath.split(xyz_high_file)
    os.makedirs(save_location, exist_ok=True)
    imagel.save(xyz_high_file)

    imageh = Image.new("RGB", (img_size, img_size))
    imageh.putdata(coordsarray_2)  # type: ignore
    save_location, _ = ntpath.split(xyz_low_file)
    os.makedirs(save_location, exist_ok=True)
    imageh.save(xyz_low_file)

    log.debug(f"XYZ maps saved to {xyz_high_file} and {xyz_low_file}")
    return rgb_file, xyz_high_file, xyz_low_file


def run_batch(directory):
    all_files = glob.glob(f"{directory}/ascii/*.xyzrgb")
    for file in all_files:
        file_name = file.split("/")[-1]
        protein = file_name.split("-")[1]
        log.debug(f"protein:{protein}, file name: {file_name}")
        file_name = file_name.replace("xyzrgb", "png")
        rgb_file = f"{directory}/MAPS/rgb/{file_name}"
        if not os.path.isfile(rgb_file):
            pcd_to_png(os.path.abspath(file), directory)
            # os.remove(file)


if __name__ == "__main__":
    import sys

    # protein = "/Users/till/Documents/UNI/Master_Bioinformatik-Universität_Wien/2.Semester/Softwareentwicklungsprojekt/Code/alphafold_to_vrnetzer/plys/AF-A0A024RBG1-F1-model_v1.ply"
    # protein = sys.argv[1]
    # pcd_to_png(protein)
    source = "/Users/till/Documents/UNI/Master_Bioinformatik-Universität_Wien/3.Semester/proteins/Multistru/Combined"
    run_batch(source)
