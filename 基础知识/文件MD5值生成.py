import hashlib
import sys
# ##暂时行无法运行，搁置###


def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        sys.exit('Usage: %s file' % sys.argv[0])

        filename = sys.argv[1]
        m = hashlib.md5()
        with open(filename, 'rb') as f:
            while True:
                f_block = fp.read(4096)
                if not f_block: break
                m.update(f_block)

        print (m.hexidigest(),filename,'123')


main()
