from conans import ConanFile, MSBuild


class TestConan(ConanFile):
    name = "test"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"


    def build(self):
        msbuild = MSBuild(self)
        definitions = {"TEST_DEFINE":None}
        msbuild.build("test.sln", upgrade_project=False, definitions=definitions, verbosity="normal")
        

