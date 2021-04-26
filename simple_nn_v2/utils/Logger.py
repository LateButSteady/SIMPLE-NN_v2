
class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self, name, fmt=':6.4e', sqrt=False):
        self.name = name
        self.fmt = fmt
        self.sqrt = sqrt
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        #self.sum += val
        self.count += n
        self.avg = self.sum / self.count

        if self.sqrt:
            self.sqrt_val = self.val**0.5
            self.sqrt_avg = self.avg**0.5

    def __str__(self):
        if self.sqrt:
            fmtstr = '{name} {sqrt_val' + self.fmt + '} ( {sqrt_avg' + self.fmt + '} )'
        else:
            fmtstr = '{name} {val' + self.fmt + '} ( {avg' + self.fmt + '} )'
        return fmtstr.format(**self.__dict__)


class ProgressMeter(object):
    def __init__(self, num_batches, meters, prefix="", suffix=""):
        self.batch_fmtstr = self._get_batch_fmtstr(num_batches)
        self.meters = meters
        self.prefix = prefix
        self.suffix = suffix

    def display(self, batch):
        entries = [self.prefix + self.batch_fmtstr.format(batch)]
        entries += [str(meter) for meter in self.meters]
        entries += [self.suffix]
        print('\t'.join(entries), flush=True)


    def log(self, batch):
        entries = [self.prefix + self.batch_fmtstr.format(batch)]
        entries += [str(meter) for meter in self.meters]
        entries += [self.suffix]
        return '\t'.join(entries)+'\n'

    def _get_batch_fmtstr(self, num_batches):
        num_digits = len(str(num_batches // 1))
        fmt = '{:' + str(num_digits) + 'd}'
        return ' Batch [' + fmt + '/' + fmt.format(num_batches) + ']'
