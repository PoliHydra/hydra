import argparse
import numpy as np
import numpy.linalg


def norm(x):
    return numpy.linalg.norm(x, ord=np.inf)


def main():
    parser = argparse.ArgumentParser(
        description='compare a numpy .npz file to a reference file')
    parser.add_argument('data', metavar='A.npz', help='file to test')
    parser.add_argument('refv', metavar='B.npz', help='reference file')

    args = parser.parse_args()

    try:
        with np.load(args.data) as data, np.load(args.refv) as ref:
            dataset = set(data.files)
            refset = set(ref.files)
            if set(data.files) != set(ref.files):
                print('missing vars in {}:'.format(args.data))
                for k in sorted(refset - dataset):
                    print('   {}'.format(k))
                print('extra vars in {}:'.format(args.data))
                for k in sorted(dataset - refset):
                    print('   {}'.format(k))
            for key in sorted(refset & dataset):
                a = data[key]
                b = ref[key]
                if a.shape == b.shape:
                    err = norm(a-b)
                else:
                    err = 'different shape'
                print('{}: {}'.format(key, err))
    except IOError as exp:
        print(exp)

if __name__ == '__main__':
    main()
