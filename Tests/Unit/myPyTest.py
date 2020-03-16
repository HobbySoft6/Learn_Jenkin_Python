import pytest
import os

#pytest.main()

if __name__ == '__main__':

    #print("my work directory is: "+ os.getcwd())
    
    working_dir = os.getcwd()
    print(working_dir)
    print("after split:  " )
    firstDir = os.path.split(working_dir)[0]
    moduleName = os.path.split(working_dir)[-1]
    print(moduleName)
    anotherDir = "--junitxml={0}".format(os.path.join(working_dir, 'reports', "xunit-result-{0}.xml".format(moduleName)))
    print(anotherDir)
    testDir = [firstDir, anotherDir]
    print(testDir)
   
    #pytest.main(testDir)