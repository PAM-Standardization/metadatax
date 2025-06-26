class DeploymentPanel {

    static div = document.getElementById('deployment-panel');
    static deploymentTitle = document.getElementById('deployment-title');
    static projectTitle = document.getElementById('project-title');
    static content = document.getElementById('deployment-content');

    /**
     * Open panel
     * @param e {{sourceTarget?: {feature?: {properties?: {deployment?: Deployment}}}}}
     * @return {void}
     */
    static open(e) {
        const deployment = e?.sourceTarget?.feature?.properties?.deployment;
        const project = PROJECTS.find(p => p.id === deployment?.project);

        if (!deployment || !project) return this.close()
        this.content.innerHTML = ''
        this.deploymentTitle.innerText = deployment.name;
        this.projectTitle.innerText = project.name;

        this.setupProject(project)
        this.setupDeployment(deployment)
        this.setupChannelConfigurations(deployment.channel_configurations)

        this.div.classList.add('open')
    }

    static close() {
        this.div.classList.remove('open')
        this.content.innerHTML = ''
    }

    /**
     * @private
     * @param state {'open' | 'close'}
     * @param id {string}
     * @return {string}
     */
    static getSectionTitleChevron(state, id) {
        return `<a onclick="DeploymentPanel.toggleSection('${id}')">
                    <ion-icon name="${state === 'open' ? 'chevron-down' : 'chevron-forward'}"></ion-icon>
                </a>`
    }

    /**
     * @private
     * @param id {string}
     * @return {void}
     */
    static toggleSection(id) {
        const section = document.getElementById(id)
        const titles = section.getElementsByTagName('h5');
        if (titles.length === 0) return;
        const icons = titles[0].getElementsByTagName('ion-icon');
        if (icons.length === 0) return;
        const isOpen = !section.classList.contains('closed');
        titles[0].innerHTML = this.getSectionTitleChevron(isOpen ? 'close' : 'open', section.id) + titles[0].innerText;
        if (isOpen) section.classList.add('closed');
        else section.classList.remove('closed');
    }


    /**
     * @param project {Project}
     * @private
     */
    static setupProject(project) {
        const projectElement = document.createElement('div')
        projectElement.id = 'project';

        projectElement.innerHTML = `<h5>${this.getSectionTitleChevron('open', 'project')}Project</h5>`

        projectElement.innerHTML += `
            <div>Name</div>
            <div>${project.name}</div>
        `
        projectElement.innerHTML += `
            <div>Contacts</div>
            <div>${project.contacts.map(cr => `${cr.contact.name} <span style="opacity: 0.5">(${cr.role})</span>`).join('<br/>')}</div>
        `
        if (project.accessibility)
            projectElement.innerHTML += `
                <div>Accessibility</div>
                <div>${project.accessibility}</div>
        `
        if (project.project_type)
            projectElement.innerHTML += `
                <div>Type of project</div>
                <div>${project.project_type.name}</div>
        `
        if (project.project_goal)
            projectElement.innerHTML += `
                <div>Goal of the project</div>
                <div>${project.project_goal}</div>
        `

        this.content.appendChild(projectElement);
    }

    /**
     * @param deployment {Deployment}
     * @private
     */
    static setupDeployment(deployment) {
        const deploymentElement = document.createElement('div')
        deploymentElement.id = 'deployment';
        deploymentElement.innerHTML = `<h5>${this.getSectionTitleChevron('open', 'deployment')}Deployment</h5>`

        deploymentElement.innerHTML += `
            <div>Name</div>
            <div>${deployment.name}</div>
        `
        deploymentElement.innerHTML += `
            <div>Contacts</div>
            <div>${deployment.contacts.map(cr => `${cr.contact.name} <span style="opacity: 0.5">(${cr.role})</span>`).join('<br/>')}</div>
        `
        if (deployment.site)
            deploymentElement.innerHTML += `
                <div>Site</div>
                <div>${deployment.site.name}</div>
        `
        if (deployment.campaign)
            deploymentElement.innerHTML += `
                <div>Campaign</div>
                <div>${deployment.campaign.name}</div>
        `
        if (deployment.deployment_date || deployment.deployment_vessel)
            deploymentElement.innerHTML += `
                <div>Deployment</div>
                <div>${[deployment.deployment_date, deployment.deployment_vessel].filter(d => !!d).join('<br/>')}</div>
        `
        if (deployment.recovery_date || deployment.recovery_vessel)
            deploymentElement.innerHTML += `
                <div>Recovery</div>
                <div>${[deployment.recovery_date, deployment.recovery_vessel].filter(d => !!d).join('<br/>')}</div>
        `
        if (deployment.description)
            deploymentElement.innerHTML += `
                <div>Description</div>
                <div>${deployment.description}</div>
        `
        if (deployment.platform)
            deploymentElement.innerHTML += `
                <div>Platform</div>
                <div>${deployment.platform.name} <span style="opacity: 0.5">(${deployment.platform.type.name})</span></div>
        `
        if (!deployment.platform.type.is_mobile) {
            deploymentElement.innerHTML += `
                <div>Coordinates</div>
                <div>${deployment.latitude}, ${deployment.longitude}</div>
            `
            if (deployment.bathymetric_depth)
                deploymentElement.innerHTML += `
                    <div>Bathymetric depth</div>
                    <div>${deployment.bathymetric_depth}</div>
                `
        }
        this.content.appendChild(deploymentElement);
    }

    /**
     * @param channels {ChannelConfiguration[]}
     * @private
     */
    static setupChannelConfigurations(channels) {
        for (const index in channels) {
            const channel = channels[index];
            const channelElement = document.createElement('div')
            channelElement.classList.add('closed')
            channelElement.id = `channel-${index}`;
            channelElement.innerHTML = `<h5>${this.getSectionTitleChevron('close', channelElement.id)}Channel ${+index + 1}</h5>`

            channelElement.innerHTML += `
                <div>Duty cycle</div>
                <div>${channel.continuous ? 'Continuous' : `${channel.duty_cycle_on}s ON - ${channel.duty_cycle_off}s OFF`}</div>
            `
            channelElement.innerHTML += `
                <div>Instrument depth</div>
                <div>${channel.instrument_depth}m</div>
            `
            if (channel.recorder_specification) {
                channelElement.innerHTML += `
                    <div>Gain</div>
                    <div>${channel.recorder_specification.gain}dB</div>
                `
                channelElement.innerHTML += `
                    <div>Sample depth</div>
                    <div>${channel.recorder_specification.sample_depth}</div>
                `
                channelElement.innerHTML += `
                    <div>Sampling frequency</div>
                    <div>${channel.recorder_specification.sampling_frequency}</div>
                `
                const recorder = channel.recorder_specification.recorder;
                channelElement.innerHTML += `
                    <div>Recorder</div>
                    <div>${recorder.model} ${recorder.serial_number}</div>
                `
                const hydrophone = channel.recorder_specification.hydrophone;
                channelElement.innerHTML += `
                    <div>Hydrophone</div>
                    <div>${hydrophone.model} ${hydrophone.serial_number}</div>
                `
                channelElement.innerHTML += `
                    <div>Hydrophone sensitivity</div>
                    <div>${hydrophone.hydrophone_specification.sensitivity}</div>
                `
            }

            this.content.appendChild(channelElement);
        }
    }
}


