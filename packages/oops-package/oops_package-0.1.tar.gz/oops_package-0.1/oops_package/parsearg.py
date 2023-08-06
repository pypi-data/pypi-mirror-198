import argparse, sys, os


# file1 = sys.argv[1]
# file2 = sys.argv[2]


class Args:
    # def __init__(self, file1, file2):
    #     self.file1 = file1
    #     self.file2 = file2

    def arg_parse(self):
        parser = argparse.ArgumentParser(usage="python %(prog)s L1.txt L2.txt R.txt",
                                         epilog="We have to select the type of set-operation before executing the program",
                                         description="Performing multiple Set Operations based on the User Input")
        # parser.add_argument("L1.txt", type=self.file_validation('L1.txt', self.file1, self.file2),help="Name of the 1st file to be processed", default="L1.txt")
        # parser.add_argument("L2.txt", type=self.file_validation('L2.txt', self.file1, self.file2),help="Name of the 2nd file to be processed", default="L2.txt")        
        parser.add_argument("L1.txt", type=self.file_validation('L1.txt'),help="Name of the 1st file to be processed", default="L1.txt")
        parser.add_argument("L2.txt", type=self.file_validation('L2.txt'),help="Name of the 2nd file to be processed", default="L2.txt")
        parser.add_argument("R.txt", help="Name of the file to be created as an end result", default="R.txt")
        args = parser.parse_args()
        return args

    # def file_validation(self, file, file1, file2):
    def file_validation(self, file):
        file_exists = os.path.isfile(file)
        try:
            # if file_exists and file in file1 or file2:
            if file_exists:
                file_not_empty = os.path.getsize(file)
                if file_not_empty:
                    print(f"{file} exists")
                else:
                    print(f"{file} of the input files must be empty, make sure to have the required data")
                    sys.exit(1)
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(file, "is not found or could be both files not found or wrong file/s is/are specified\nMake sure "
                        "to have the required input files present.")
            sys.exit(1)


if __name__ == "__main__":
    try:
        Args().arg_parse()
        sys.exit(0)
    except Exception as e1:
        print('COMMAND FAILURE: {0}'.format(str(e1)))
        import traceback
        traceback.print_exc()
        sys.exit(1)
        
