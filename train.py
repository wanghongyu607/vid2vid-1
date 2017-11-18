import time , os ,cv2
from options.train_options import TrainOptions
from data.data_loader import CreateDataLoader
from models.models import create_model
#from util.visualizer import Visualizer
from PIL import Image
import ntpath
import numpy as np
opt = TrainOptions().parse()
data_loader = CreateDataLoader(opt)
dataset = data_loader.load_data()
print(dataset)
dataset_size = len(data_loader)
print('#training videos = %d' % dataset_size)
from make_video import save_video
model = create_model(opt)
#visualizer = Visualizer(opt)
total_steps = 0
web_dir = os.path.join(opt.results_dir, opt.name, '%s_%s' % (opt.phase, opt.which_epoch))
def ck_array(i,o):
    i_A = np.transpose(127.5*(i['A']+1.)[0],(1,2,3,0))
    i_B = np.transpose(127.5*(i['B']+1.)[0],(1,2,3,0))
    o_A = o['real_A']
    o_B = o['real_B']
    a_diff = i_A - o_A
    b_diff = i_B - o_B
    print('diffa',a_diff.max(),a_diff.min(),a_diff.mean())
    print('diffb', b_diff.max(), b_diff.min(), b_diff.mean())


def save_videos(web_dir, visuals, vid_path):
    vid_dir = os.path.join(web_dir, 'videos')
    short_path = ntpath.basename(vid_path[0])
    # name = os.path.splitext(short_path)[0]
    name = vid_path.split('.')[-2].split('/')[-1] + str(int(time.time()))
    # print(233333,[i for i in vid_path.split('.')])
    #save_video(visuals,name, dir_path = 'log')



    for label, vid_numpy in visuals.items():
        vid_name = '%s_%s' % (label, name)
        #print(vid_name)
        save_path = vid_dir
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        #print(vid_numpy.shape)


        for i in range(vid_numpy.shape[0]):
            #print(vid_numpy[i].shape)
            p = 'save',save_path + "/label/" + str(i) + vid_name+".png"
            print(p)
            #cv2.imwrite(save_path + "/label/" + str(i) + vid_name+".png", vid_numpy[i])
            cv2.imwrite(save_path + "/label/" + str(i)  + ".png", vid_numpy[i])
            print('save_img_shape',vid_numpy[i].shape)
            # im = Image.fromarray(vid_numpy[i],'RGB')
            # im.save(save_path + "_" + str(i) + ".png")


for epoch in range(opt.epoch_count, opt.niter + opt.niter_decay + 1):
    epoch_start_time = time.time()
    epoch_iter = 0

    for i, data in enumerate(dataset):

        #print(data.shape())

        iter_start_time = time.time()
        #visualizer.reset()
        total_steps += opt.batchSize
        epoch_iter += opt.batchSize
        model.set_input(data)
        model.optimize_parameters()

        if total_steps % opt.display_freq == 0:
            save_result = total_steps % opt.update_html_freq == 0

            visuals = model.get_current_visuals()
            #ck_array(data, visuals)
            vid_path = model.get_image_paths()
            # print(visuals)
            print('process video... %s' % vid_path)
            save_videos(web_dir, visuals, vid_path)

        if total_steps % opt.print_freq == 0:
            errors = model.get_current_errors()
            t = (time.time() - iter_start_time) / opt.batchSize
            #visualizer.print_current_errors(epoch, epoch_iter, errors, t)
            #if opt.display_id > 0:
                #visualizer.plot_current_errors(epoch, float(epoch_iter)/dataset_size, opt, errors)

        if total_steps % opt.save_latest_freq == 0:
            print('saving the latest model (epoch %d, total_steps %d)' %
                  (epoch, total_steps))
            model.save('latest')

    if epoch % opt.save_epoch_freq == 0:
        print('saving the model at the end of epoch %d, iters %d' %
              (epoch, total_steps))
        model.save('latest')
        model.save(epoch)

    print('End of epoch %d / %d \t Time Taken: %d sec' %
          (epoch, opt.niter + opt.niter_decay, time.time() - epoch_start_time))
    model.update_learning_rate()
