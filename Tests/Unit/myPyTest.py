import pytest
import os

#pytest.main()

if __name__ == '__main__':

    #print("my work directory is: "+ os.getcwd())
    testDir = [os.getcwd()+"\Tests"]
    
    working_dir = os.getcwd()
    moduleName = os.path.split(working_dir)[-1]
    anotherDir = "--junitxml={0}".format(os.path.join(working_dir, 'reports', "xunit-result-{0}.xml".format(moduleName)))
    print(anotherDir)
    print('aaaaaaaaaaaaa')
    pytest.main(testDir, anotherDir)