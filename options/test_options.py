from .base_options import BaseOptions


class TestOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        self.parser.add_argument('--ntest', type=int, default=float("inf"), help='# of test examples.')
        self.parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
        self.parser.add_argument('--aspect_ratio', type=float, default=1.0, help='aspect ratio of result images')
        self.parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
        self.parser.add_argument('--which_epoch', type=str, default='latest', help='which epoch to load? set to latest to use latest cached model')
        self.parser.add_argument('--how_many', type=int, default=50, help='how many test images to run')
        #self.parser.add_argument('--identity', type=float, default=0.0, help='use identity mapping. Setting identity other than 1 has an effect of scaling the weight of the identity mapping loss. For example, if the weight of the identity loss should be 10 times smaller than the weight of the reconstruction loss, please set optidentity = 0.1')
        self.parser.add_argument('--data_dir', type=str, default='/data/dataset/depthdata/vkitti_1.3.1_rgb/**/**/',
                                 help='video or images data repository, example: virtualkitti dataset = /data/dataset/depthdata/vkitti_1.3.1_rgb/**/**/ | babayCrawlling dataset: /data/dataset/UCF/v_BabyCrawling**.avi')
        self.parser.add_argument('--depth', type=int, default=76, help='3D Video frames length for both A and B;2018.1.1change to double,this should be doubel actual depth')
        self.parser.add_argument('--skip', type=int, default=1, help='skip how many frames to catch data')
        self.parser.add_argument('--load_video', type=int, default=0, help='load video = 1 | load image = 0')
        self.isTrain = False
        self.parser.add_argument('--display_freq', type=int, default=50, help='frequency of showing training results on screen')
        self.parser.add_argument('--display_single_pane_ncols', type=int, default=0, help='if positive, display all images in a single visdom web panel with certain number of images per row.')
        self.parser.add_argument('--update_html_freq', type=int, default=1000, help='frequency of saving training results to html')
        self.parser.add_argument('--print_freq', type=int, default=5, help='frequency of showing training results on console')
        self.parser.add_argument('--save_latest_freq', type=int, default=2000, help='frequency of saving the latest results')
        self.parser.add_argument('--save_epoch_freq', type=int, default=1, help='frequency of saving checkpoints at the end of epochs')
        self.parser.add_argument('--continue_train', action='store_true', help='continue training: load the latest model')
        self.parser.add_argument('--epoch_count', type=int, default=1, help='the starting epoch count, we save the model by <epoch_count>, <epoch_count>+<save_latest_freq>, ...')
        self.parser.add_argument('--debug', type=int, default=0, help='print more info')
        # self.parser.add_argument('--which_epoch', type=str, default='latest', help='which epoch to load? set to latest to use latest cached model')
        self.parser.add_argument('--niter', type=int, default=100, help='# of iter at starting learning rate')
        self.parser.add_argument('--niter_decay', type=int, default=100, help='# of iter to linearly decay learning rate to zero')
        self.parser.add_argument('--beta1', type=float, default=0.5, help='momentum term of adam')
        self.parser.add_argument('--lr', type=float, default=0.0002, help='initial learning rate for adam')
        self.parser.add_argument('--no_lsgan', action='store_true', help='do *not* use least square GAN, if false, use vanilla GAN')
        self.parser.add_argument('--lambda_A', type=float, default=10.0, help='weight for cycle loss (A -> B -> A)')
        self.parser.add_argument('--lambda_B', type=float, default=10.0, help='weight for cycle loss (B -> A -> B)')
        self.parser.add_argument('--pool_size', type=int, default=50, help='the size of image buffer that stores previously generated images')
        self.parser.add_argument('--no_html', action='store_true', help='do not save intermediate training results to [opt.checkpoints_dir]/[opt.name]/web/')
        self.parser.add_argument('--lr_policy', type=str, default='lambda', help='learning rate policy: lambda|step|plateau')
        self.parser.add_argument('--lr_decay_iters', type=int, default=50, help='multiply by a gamma every lr_decay_iters iterations')
        self.parser.add_argument('--identity', type=float, default=0.5, help='use identity mapping. Setting identity other than 1 has an effect of scaling the weight of the identity mapping loss. For example, if the weight of the identity loss should be 10 times smaller than the weight of the reconstruction loss, please set optidentity = 0.1')
        ## add load data option
        # self.parser.add_argument('--gpu_ids', type=str, default='0,1,2', help='gpu ids: e.g. 0  0,1,2, 0,2. use -1 for CPU')
        # self.parser.add_argument('--name', type=str, default='experiment_name', help='name of the experiment. It decides where to store samples and models')
        # self.parser.add_argument('--dataset_mode', type=str, default='unaligned', help='chooses how datasets are loaded. [unaligned | aligned | single | v]')
        # self.parser.add_argument('--model', type=str, default='cycle_gan',
        #                          help='chooses which model to use. cycle_gan, pix2pix, test')
        # self.parser.add_argument('--which_direction', type=str, default='AtoB', help='AtoB or BtoA')
        # self.parser.add_argument('--nThreads', default=2, type=int, help='# threads for loading data')
        # self.parser.add_argument('--checkpoints_dir', type=str, default='./checkpoints', help='models are saved here')
        # self.parser.add_argument('--norm', type=str, default='instance', help='instance normalization or batch normalization')
        # self.parser.add_argument('--serial_batches', action='store_true', help='if true, takes images in order to make batches, otherwise takes them randomly')
        # self.parser.add_argument('--display_winsize', type=int, default=256,  help='display window size')
        # self.parser.add_argument('--display_id', type=int, default=1, help='window id of the web display')
        # self.parser.add_argument('--display_port', type=int, default=8097, help='visdom port of the web display')
        # self.parser.add_argument('--no_dropout', action='store_true', help='no dropout for the generator')
        # self.parser.add_argument('--max_dataset_size', type=int, default=float("inf"), help='Maximum number of samples allowed per dataset. If the dataset directory contains more than max_dataset_size, only a subset is loaded.')
        # self.parser.add_argument('--resize_or_crop', type=str, default='resize_and_crop', help='scaling and cropping of images at load time [resize_and_crop|crop|scale_width|scale_width_and_crop]')
        # self.parser.add_argument('--no_flip', action='store_true', help='if specified, do not flip the images for data augmentation')
        # self.parser.add_argument('--init_type', type=str, default='xavier', help='network initialization [normal|xavier|kaiming|orthogonal]')
        # self.parser.add_argument('--input_num', type = int, default = 1,help = 'input num ,if only rgbd ,num =1, if add more sensor ,num = 2 or more')
        # self.parser.add_argument('--sensor_types', type = str, default = '',  help = 'angle,speedX,speedY')
