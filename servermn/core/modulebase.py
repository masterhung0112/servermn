class modulebase:
    name = None
    title = None

    __init__(self, name, title):
        """
        @param name String module's name
        @param title The module's title
        Exception if no name is provided
        """
        this.name = name
        this.title = title

    def info(self):
        """Read module information from YAML file
        """
        pass
    
    def depends(self):
        """Return an array with the names of the modules that
        this module depends on

        @returns array ref holding the names of the modules that the request modules
        """
        return []
    
    def initialsetup(self, version):
        """This method is run to carry out the actions that are needed
        when the module is installed or upgraded

        The run of this method must be always idempotent.
        So the actions will need to check if they are necessary
        or not to avoid problems when executed on upgrades.

        The default implementation is to call the following script
        if exists and has execution rights:
            /usr/share/xxx-module/initial-setup
        
        But this method can be overriden by any module.
        When upgrading ,the version of the previously installed
        package is pass as arugment

        @param version version of the previous package or undef
                if this is the first install
        """
        pass
    
    def migrate(self, version):
        """This method runs all the needed migrations on an module upgrade

        The migration scripts need to be located at
            /usr/share/xxx-module/migration/[00-99].xx
        
        @param version version of the previous package
        """
        pass
    
    def revokeconfig(self):
        """Base method to revoke config.
        It just notifies that the module has been restarted.
        It should be overriden by subclasses as needed.
        """
        pass
    
    def save(self):
        """Sets a module as saved. This implies a call to regenConfig and 
            set the module as saved and unlock it
        """
        pass
    
    def saveconfig(self):
        """Save module config, but do not call regenconfig
        """
        pass
    
    def saveconfigrecursive(self):
        """Save module config and the modules which depends on recursively
        """
        pass
    
    def changed(self):
        """Returns whether the module has changes status or not
        """
        pass
    
    def setaschanged(self, newchangedstatus = True):
        """Sets the module changed status
        @param newchangedstatus options, default to true (changed)
        """
        pass
    
    def makebackup(self, dir, bug):
        """Restore the module state from a backup

        @param dir directory used for the backup operation (named parameters following)
        @param bug whether we are making a bug report instead of a normal backup
        """
        pass
    
    def backupdir(self, dir):
        """
        @param dir directory used for restore/backup operation
        "return the path to the directory used by the module to dump or restore his state
        """
        pass
    
    def createbackupdir(self, dir):
        """Creates a directory to dump or restore files containing the module state.
        If there are already an appropriate directory, it simply returns the path of this directory
        """
        pass

    def restorebackup(self, dir):
        """Restore the module state from a backup
        @param dir directory used for the restore operation
        """
        pass
    
    def menu(self):
        """ This method returns the menu for the module.
        What it returns it will be added up to the interface's menu.
        It should be overriden by subclasses as needed
        """
        return None
    
    def widgets(self):
        """Return the widget names for the module. It should be overriden by subclasses as needed

        @returns An array of hashes containing keys 'title' and 'widget'.
                'title' being the title of the widget and
                'widget' a function that can fill an
                Dashboard::Widget that will be passed as a parameter.
                It can optionally have the key 'default' set to 1 to have the widget
                added by default to the dashboard the first time it's seen.
                It can also contain a 'parameter' key which will be passed as parameter
                to the widget function. This is intended to allow the dynamic creation of several widgets.
        """
        return []
    
    def widget(self, name):
        """Return the appropriate widget if exists or None otherwise

        @param name the widget name
        @returns Widget with the appropriate widget
        """
        return None
    
    def package(self):
        """Return the package name
        """
        return "servermn-" + self.name

    def version(self):
        """Return the package version
        """
        return self.version
    
    def wizardpages(self):
        """Return an array ref containing the wizard pages for the module.
        It should be overriden by subclasses as needed.

        @returns An array ref of URL's of wizard pages for this module.
        This pages must be implemented using WizardPage as base class

        Example:
            [
                {
                    page: "/Module/Wizard/Page"
                    order: 201
                }
            ]
        """
        return []
    
    def aroundRestoreConfig(self, dir, extraoption):
        """Wraps the restoreconfig call.
        The purpose of this sub is to allow specila types of modules
        like Module::Config to call another method alongside with restoreconfig transparently
        normally modules does not need to override this.

        @param dir directory where are located the backup files
        """
        self.restoreconfig(dir, extraoption)
        pass