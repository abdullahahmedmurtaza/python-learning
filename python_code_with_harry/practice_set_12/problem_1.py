try:

    with (
        open('file1.txt','r') as f1,
        open('file2.txt','r') as f2,
        open('file3.txt','r') as f3,
    ) :
        f1_content = f1.read()
        f2_content = f2.read()
        f3_content = f3.read()
except Exception as e:
    print('file not found')
    

print('after the files context')