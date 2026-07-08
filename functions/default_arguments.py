def default_arg(maths,sci,hindi,kannada =0):
    print(f"maths= {maths}")
    print(f"science= {sci}")
    print(f"hindi= {hindi}")
    print(f"kannada= {kannada}")
    total_marks = maths + sci + hindi + kannada
    print(f"Total Marks= {total_marks}")
default_arg(100,85,67)
