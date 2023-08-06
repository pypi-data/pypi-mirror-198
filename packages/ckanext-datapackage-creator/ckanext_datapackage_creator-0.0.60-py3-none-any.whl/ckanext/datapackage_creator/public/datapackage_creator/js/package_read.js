try {
    var app = new Vue({
        delimiters: ['[[', ']]'],
        el: '#additional-app',
        data: {
            package_id: '',
            frequency: '',
            profile: '',
            contributors: []
        },
        mounted () {
            this.package_id = this.$refs.packageId.value
            this.getPackage()
        },
        methods: {
            getPackage() {
                const url = `/datapackage-creator/show-datapackage/${this.package_id}`
                axios.get(url).then(res => {
                    let data = JSON.parse(res.data.datapackage.data)
                    this.profile = data.type
                    this.frequency = data.frequency
                    this.contributors = data.contributors
                })
            }
        }
    })
} catch (error) {}

try {
    const validation_badge = document.getElementById('badge-validation')
    const package_id = validation_badge.getAttribute('data-package-id')
    const url_datapackage = `/datapackage-creator/show-datapackage/${package_id}`
    axios.get(url_datapackage).then(res => {
        if(res.data.datapackage) {
            let data = JSON.parse(res.data.datapackage.errors_json)
            if(data && data.valid) {
                let success_badge = document.getElementById('datapackage-valid')
                success_badge.setAttribute('style', '')
            } else if(data && !data.valid) {
                let error_badge = document.getElementById('datapackage-invalid')
                error_badge.setAttribute('style', '')
            }
        }
    })
} catch (error) {
    
}

try {
    const downloadButton = document.getElementById('btn-download')
    const selectAllResources = document.getElementById('select-all-resources')
    selectAllResources.addEventListener('click', e => {
        const checked = selectAllResources.checked
        const resources = document.getElementsByClassName('check-resource')
        for (let index = 0; index < resources.length; index++) {
            const element = resources[index];
            element.checked = checked
        }
    })
} catch(error) {}