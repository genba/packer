Vagrant.configure("2") do |config|
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"

    config.vm.define :core do |core|
	    core.vm.synced_folder "core/", "/home/vagrant/core/"
   end

    config.vm.define :web do |web|
        web.vm.synced_folder "web/", "/home/vagrant/web/"
        web.vm.network :forwarded_port, host: 8000, guest: 8000
        web.vm.provision :shell, :path => "web/bootstrap.sh"
    end
end
