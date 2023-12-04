import torch

def verify_args(args):
    if args.use_cuda and torch.cuda.is_available() == False:
        print("--CUDA is not available.--")
        exit(0)

    if args.thickness < 1 / args.resize_window:
        print("--arguments error--")
        exit(0)

    if not (0 < args.region[0] <= 1) and not (0 < args.region[1] <= 1):
        print("--region out of range(0 ~ 1)--")
        exit(0)

    if args.lock_button not in ['left', 'middle', 'right', 'x1', 'x2']:
        print("--lock_button is unsupported: (left, middle, right, x1, x2) only--")
        exit(0)

    for i in args.lock_choice:
        if i not in args.lock_tag:
            print("--lock arguments error--")
            exit(0)

    buttons = []
    buttons.append(args.lock_button)