
module Masspectrum
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/''_masspectrum.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "masspectrum",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "async-masspectrum.js",
    external_url = "https://unpkg.com/masspectrum@0.0.1/masspectrum/async-masspectrum.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-masspectrum.js.map",
    external_url = "https://unpkg.com/masspectrum@0.0.1/masspectrum/async-masspectrum.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "masspectrum.min.js",
    external_url = "https://unpkg.com/masspectrum@0.0.1/masspectrum/masspectrum.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "masspectrum.min.js.map",
    external_url = "https://unpkg.com/masspectrum@0.0.1/masspectrum/masspectrum.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
