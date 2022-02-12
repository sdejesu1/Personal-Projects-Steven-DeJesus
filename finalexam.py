import random

SAMPLES_FILE = 'samples.txt'


def main():
    """ Call generate_random_samples with the range of samples to generate
    (low, high), as well as the quantity of samples to produce """
    generate_random_samples(0, 10, 100)


def generate_random_samples(low, high, samples):
    """ Generate the quantity of random integer samples in the range 
    specified (low, high) and write to text file """
    try:
        out_file = open(SAMPLES_FILE, 'w')
        for _ in range(samples):
            val = random.randint(low, high)
            out_file.write(str(val) + '\n')
        out_file.close()
    except IOError:
        print('Error opening file.')
    except ValueError:
        print('Invalid values provided.')
    except TypeError:
        print('Error writing samples to file.')
    else:
        print('Success: Data written to file.')


if __name__ == '__main__':
    main()
