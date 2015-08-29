
import functools

class Test_DependencyRegister__construction__public_api:

    def test__creating_new__should_succeed(self, dep_reg):
        pass

class Test_DependencyRegister_register__public_api:

    def test__giving_only_resource_name__should_succeed(
            self, dep_reg, fake_resource_name):
        dep_reg.register(fake_resource_name)

    def test__giving_only_resource_name__should_give_partial(
            self, dep_reg, fake_resource_name):

        result = dep_reg.register(fake_resource_name)

        # register() should give a partial of itself with one arg fixed
        assert isinstance(result, functools.partial)
        assert result.func == dep_reg.register
        assert result.args == (fake_resource_name,)

    def test__giving_resource_name_and_dependent__should_succeed(
            self, dep_reg, fake_resource_name, fake_dependent):
        dep_reg.register(fake_resource_name, fake_dependent)

    def test__giving_resource_name_and_dependent__should_return_dependent(
            self, dep_reg, fake_resource_name, fake_dependent):
        '''
        When called with a resource name and a dependent, register()
        should return the given dependent.

        This behaviour allows use of register() as a decorator.
        '''
        result = dep_reg.register(fake_resource_name, fake_dependent)
        assert result == fake_dependent

    def test__registering_new_dependent__should_add_dependent(
            self, dep_reg, fake_resource_name, fake_dependent):
        '''
        After calling register() with a resource name and dependent,
        instance.dependents should contain dependent.
        '''
        dep_reg.register(fake_resource_name, fake_dependent)
        assert fake_dependent in dep_reg.dependents

    def test__registering_new_dependent__should_add_resource_name_under_dependent(
            self, dep_reg, fake_resource_name, fake_dependent):
        '''
        After calling register() with a resource name and dependent,
        the instance.dependents[dependent] should contain resource name.
        '''
        dep_reg.register(fake_resource_name, fake_dependent)
        resources_dependent_on = dep_reg.dependents.get(fake_dependent)
        assert fake_resource_name in resources_dependent_on
