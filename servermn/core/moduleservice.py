import moduleconfig

class moduleservice(moduleconfig):
    def usedfiles(self):
        """This method is mainly used to show information to the user
        about the files which are going to be modified by the service
        managed by servermn

        @returns An array ref of hashes containing the following:
            file - file's path
            reason - some info about why you need to modify the file
            module - module's name
        Example:
            [
                {
                    'file': '/etc/samba/smb.conf',
                    'reason': 'The file sharing module need to modify it',
                    'module': samba
                }
            ]
        """
        return []
    
    def actions(self):
        """This method is mainly used to show information to the user
        about the actions that need to be carried out by the service
        to configure the system

        @returns An array of hashes containing the following:
            action - action to carry out
            reason - some info about why you need to modify the file
            module - module's name
        Example:
            [
                {
                    'action': 'remove samba init script',
                    'reason': 'Will take care of start and stop the service',
                    'module': samba
                }
            ]
        """
        return []
    
    def enableactions(self):
        """Carry out the actions that are needed to enable a module.
        It usually executes those which are returned by actions.

        For example: it could remove the samba init script

        The default implemention is to call the following
        script if exists and has execution rights:
            /usr/share/servermn-module/enable-module
        
        But this method can be overriden by any module
        """
        pass
    
    def disableactions(self):
        """Run to rollback the actions that have been carried out
        to enable a module
        For example: it could restore the samba init script
        """
        pass
    
    def disablemoddepends(self):
        """Get the list of modules to be disabled when this module is disabled.
        It doesn't state a configuration dependency, it states a working dependency.

        For example: the firewall module has to be disabled together with the network module

        @returns array containing the module names
        """
        pass
    
    def enablemoddepends(self):
        """This method is used to declare which modules need to be enabled to use this module
        It doesn't state a configuration dependency, it states a working dependency.

        Example: The firewall module needs the network module.

        By default it returns the modules established in the enable depends list
        in the module YAML file. Override the method if you need something more specific,
        e.g., having a dynamic list.
        @returns array containing the dependencies names
            [ 'firewall', 'samba' ]
        """
        pass
    
    def enablemoddependsrecursive(self):
        """This method works like enablemoddepends but its recurse in all module dependencies
        @returns list reference with the dependencies names
        """
        pass
    
    def bootdepends(self):
        """This method is used to declare which modules need to 
        have its daemons started before this module runs.

        It doesn't state a configuration dependency, it states a boot dependency.

        For example: the samba module needs the printer daemon started before.

        By default it returns the modules established in the bootdepends list
        in the module YAML file. Override the method if you need something more specific.
        If nothing is specified in the YAML file nor the method is overriden, 
        the enabledepends value is returned to provide compatibility with the previous behaviour.
        @returns array containing the dependencies.
        """
        return self.enablemoddepends()
    
    def configured(self):
        """This method is used to check if the module has been configured.
        Configuration is done one time per service package version.

        If this method returns true it means that the user has accepted to
        carry out the actions and file modifications that enabling a
        service implies.

        If you must store this value in the status branch of conf in case
        you decide to override it

        @returns boolean
        """
        pass
    
    def setconfigured(self, status):
        """This method is used to set if the module has been configured.
        Configuration is done once per service package version.

        If it's set to true it means that the user has accepted
        to carry ou the actinos and file modifications that enabling a service implies.

        If you must store this value in the status branch of conf in case
        you decide to overide it

        @param boolean true if configured, false otherwise
        """
        pass