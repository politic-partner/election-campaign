# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '日本の選挙運動'
copyright = '2023 politic-partner'
author = 'politic-partner'

github_user = 'politic-partner'
github_repo = 'election-campaign'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_toolbox.collapse',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for MyST -------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    'attrs_inline',
    'attrs_block',
    'colon_fence',
    'deflist',
    'substitution',
    'tasklist',
]

myst_substitutions = {
    'github_url': f'[GitHub](https://github.com/{github_user}/{github_repo})',
    'github_discussions': f'[ディスカッション](https://github.com/{github_user}/{github_repo}/discussions)',
    'github_issues': f'[Issues](https://github.com/{github_user}/{github_repo}/issues)',
    'github_pulls': f'[プルリクエスト](https://github.com/{github_user}/{github_repo}/pulls)',
    'spread_campaign_research_questions': '[選挙調査質問集](https://docs.google.com/spreadsheets/d/1mG2GSFCkB9EkHJ0VOBqDsBvKg5BNzScpOYgtIZYoRkU/edit?usp=sharing)',
    'political_campaign_planning_manual_en_warning': """```{admonition} **Warning** This Manual Cannot Be Directly Applied to Japanese Electoral Campaigns
:class: warning
For more details, please see [notes](index).
```""",
    'political_campaign_planning_manual_ja_warning': """```{admonition} **警告** このマニュアルを日本の選挙運動へ直接適用することはできません。
:class: warning
詳しくは[注意点](index)を参照してください。
```""",
}

myst_heading_anchors = 3

myst_html_meta = {
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_js_files = [
    'js/external_link.js'
]
html_css_files = [
    'css/drawio.css',
    'css/custom.css',
]

html_title = '日本の選挙運動'

html_theme = 'furo'
html_theme_options = {
    "footer_icons": [
        {
            "name": "CC BY 4.0",
            "url": "https://creativecommons.org/licenses/by/4.0/deed.ja",
            "html": """
            <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 64 64">
                <path d="M31.957,0.311c-8.682,0-16.322,3.213-22.226,9.203C3.653,15.678,0.354,23.666,0.354,32c0,8.422,3.212,16.236,9.29,22.313c6.078,6.078,13.978,9.377,22.313,9.377c8.334,0,16.409-3.299,22.66-9.463c5.904-5.817,9.029-13.544,9.029-22.227c0-8.595-3.125-16.408-9.116-22.399C48.453,3.523,40.639,0.311,31.957,0.311z M32.043,6.041c7.12,0,13.458,2.691,18.406,7.641c4.862,4.861,7.466,11.286,7.466,18.318c0,7.119-2.518,13.371-7.379,18.146c-5.123,5.035-11.721,7.727-18.493,7.727c-6.858,0-13.283-2.691-18.232-7.641C8.862,45.283,6.084,38.772,6.084,32c0-6.858,2.778-13.369,7.727-18.406C18.673,8.646,24.924,6.041,32.043,6.041z"/>
                <path id="c" d="M31.635,26.734c-1.79-3.264-4.844-4.563-8.389-4.563c-5.16,0-9.267,3.65-9.267,9.828c0,6.283,3.861,9.829,9.442,9.829c3.581,0,6.635-1.966,8.319-4.949l-3.931-2.001c-0.878,2.105-2.212,2.738-3.896,2.738c-2.914,0-4.248-2.422-4.248-5.617c0-3.193,1.124-5.616,4.248-5.616c0.842,0,2.527,0.456,3.51,2.563L31.635,26.734z"/>
                <use xlink:href="#c" transform="translate(18.281)"/>
            </svg>
            """,
            "class": "",
        },
    ],
    "sidebar_hide_name": True,
    "light_logo": "logo_light.png",
    "dark_logo": "logo_dark.png",
    "light_css_variables": {
        "admonition-font-size": "unset",
        "admonition-title-font-size": "unset",
    },
}

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
        "sidebar/variant-selector.html",
    ]
}

html_context = {
    'github_user': github_user,
    'github_repo': github_repo,
}
