# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['embedit',
 'embedit.behaviour',
 'embedit.behaviour.prompts',
 'embedit.behaviour.search',
 'embedit.behaviour.search.pipeline_components',
 'embedit.behaviour.search.pipeline_components.a01_gather',
 'embedit.behaviour.search.pipeline_components.a02_split',
 'embedit.behaviour.search.pipeline_components.a03_process',
 'embedit.behaviour.search.pipeline_components.a03_process.edit',
 'embedit.behaviour.search.pipeline_components.a03_process.search',
 'embedit.behaviour.search.pipeline_components.a04_combine',
 'embedit.behaviour.search.pipeline_components.a05_save',
 'embedit.behaviour.search.pipelines',
 'embedit.cli',
 'embedit.structures',
 'embedit.utils']

package_data = \
{'': ['*']}

install_requires = \
['delegatefn>=0.3.4,<0.4.0',
 'dir2md>=0.2.1,<0.3.0',
 'gitpython>=3.1.30,<4.0.0',
 'numpy>=1.24.2,<2.0.0',
 'openai>=0.27.2,<0.28.0',
 'rich>=13.0.0,<14.0.0',
 'tenacity>=8.1.0,<9.0.0',
 'tiktoken>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['embedit = embedit.cli:main']}

setup_kwargs = {
    'name': 'embedit',
    'version': '0.2.11',
    'description': '',
    'long_description': '# embedit\n\n`embedit` is a command line tool for performing bulk operations on text files (e.g. a package) with OpenAI\'s API. It currently provides these commands: `search`, which performs semantic search on text files using embeddings, and `transform` which performs arbitrary transformations using a custom prompt.\n `commit-msg` generates a commit message based on the diff of the staged files and the commit history.\n `autocommit` generates a commit message and commits the changes in one step.\n\n\n## Installation\n\nInstall `embedit` using `pip`:\n\n```bash\npip install embedit\n```\n\nThis will install `embedit` and its dependencies, including `openai`. You will also need to set the `OPENAI_API_KEY` environment variable to your OpenAI API key if you haven\'t already done so.\n\n## Usage\n\n### Search\n\n`embedit search` performs semantic searches on text files. You specify a search query and a list of text files to search, `embedit` will fetch text from the files, split them into segments, embed them using OpenAI\'s API, and print them out in order of cosine distance to the query.\n\n```bash\nembedit search "search query" file1.txt file2.txt ...\n```\n\n#### Options\n\n- `--order`: the order in which the results should be displayed (ascending or descending by similarity score). Default: `ascending`.\n\n- `--top-n`: the number of top results to display. Default: `3`.\n\n- `--threshold`: a similarity threshold below which results should be filtered out. Default: `0.0`.\n\n- `--frament_lines`: the target fragment length in number of lines. Default: `10`.\n\n- `--min_fragment_lines`: the minimum fragment length in number of lines. Default: `0`.\n\n### Transform\n\nThe `transform` command allows you to transform one or more text files by passing their markdown representation with a given prompt to the OpenAI API.\n\n```bash\nembedit transform **/*.py --prompt "Add a docstring at the top of each file" --output-dir out\n```\n\n*Can\'t I just feed my files to the API directly?*\n\nYou could. But transforming each file independently could lead to inconsistent behaviour. `embedit transform` combines your files into a single prompt so that they can be transformed in a coherent way and then splits the result back into individual files.\n\n#### Options\n\n- `--files`: One or more text files to transform.\n- `--transformation_fn`: The function to apply on the files.\n- `--output_dir` : The directory to save the transformed files.\n- `--yes`: Don\'t prompt before creating or overwriting files.\n- `--model`: The OpenAI API model to use.\n- `--verbose`: Whether to print verbose output.\n- `--max_chunk_len`: The maximum length (in characters) of chunks to pass to the OpenAI API.\n\n### Generate commit message\n\nThe `commit-msg` command will generate a commit message based on the diff of the staged files and the commit history. \n\nTo use it, you can run it directly:\n\n```bash\nembedit commit-msg\n```\n\nTo generate and commit the changes in one step, you can use the `autocommit` command:\n\n```bash\nembedit autocommit\n```\n\nI haven\'t tried to add `commit-msg` as a git hook, but I imagine it would work.\n\n#### Options\n\n- `--path`: The path to diff against.\n- `--max-log-tokens`: The maximum number of tokens to include in the commit message.\n- `--max-diff-tokens`: The maximum number of tokens to include in the diff.\n- `--max-output-tokens`: The maximum number of tokens to include in the OpenAI API output.\n- `--model`: The OpenAI API model to use.\n- `--num-examples`: The number of examples to use.\n- `--use-builtin-examples`: Whether to use the built-in examples.\n- `--hint`: A hint to pass to the OpenAI API.\n- `--verbose`: Print verbose output.\n- `--git-params`: Keyword arguments to pass to the git commit command.\n\n\nFor example, the below command will generate a commit message using `gpt-3.5-turbo`, passing a hint that the document parameters have been updated, and will use not any of your previous commits as examples. The latter option is useful if your past commit messages have suffered *neglect*.\n\n```bash\nembedit autocommit --model "gpt-3.5-turbo" --hint "doc params" --num-examples 0\n```\n## Tips\n\n### Wildcards\nYou can also use wildcards to specify a pattern of files to search in. Here\'s an example of how you can use the `**` wildcard to search for Python files in all directories in the current directory and its subdirectories:\n\n```bash\nembedit search "query" **/*.py\n```\n\nBear in mind that the behavior of the `*` and `**` wildcards may vary depending on your operating system and the terminal shell you\'re using.\n\n### Autocommit workflow\n\nI like to use the following alias, `qc` (quick commit) to automatically generate and commit changes:\n\n```bash\nalias qc="embedit autocommit --num-examples 0 --model \\"gpt-3.5-turbo\\""\n```\n\nExample usage:\n\n```bash\nqc -h "hint hint"\n```\n\nThen, when it gets something wrong, I edit the commit message and run `git commit --amend` to fix it.\n\n## Contributing\n\nIf you find a bug or want to contribute to the development of `embedit`, you can create a new issue or submit a pull request.\n\n## License\n\n`embedit` is released under the MIT license. Do whatever you want with it.',
    'author': 'IsaacBreen',
    'author_email': 'mail@isaacbreen.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
