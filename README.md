# Stop-Words-List

[About](#stop-words-list) | [How to contribute](#how-to-contribute?) | [Rules](#contributing-rules) 
:---:|:---:|:---:

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub contributors](https://img.shields.io/github/contributors/ddhira123/Stop-Words-List.svg)](https://GitHub.com/ddhira123/Stop-Words-List/graphs/contributors/) ![GitHub Hacktoberfest combined status](https://img.shields.io/github/hacktoberfest/2020/ddhira123/Stop-Words-List) ![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-yellow.svg?style=flat)![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![](https://img.shields.io/github/repo-size/ddhira123/Stop-Words-List.svg?label=Repo%20size&style=flat-square)&nbsp; ![Maintenance](https://img.shields.io/maintenance/yes/2020)![GitHub forks](https://img.shields.io/github/forks/ddhira123/Stop-Words-List?style=social) ![GitHub Repo stars](https://img.shields.io/github/stars/ddhira123/Stop-Words-List?style=social) 
</p>
A beginner friendly project to help you in open source contributions. An attempt to bring the stop words lists from all languages around the world.

## What is stop word?
[`^ back to top ^`](#)

> In computing, stop words are words which are filtered out before or after processing of natural language data. <br><br>
> \- *Wikipedia* -

In SEO terminology, stop words are the **most common words** that most search engines avoid, for the purposes of saving space and time in processing of large data during crawling or indexing. This helps search engines to save space in their databases. For example, **at**, **which**, **is**, **the**, **and** are some words categorized as stop words.

## How to Contribute?
[`^ back to top ^`](#)

There are 3 ways to contribute in this repo:

- Add new stop words list file. 
- Edit and do some improvements to existing stop words list.
- Enhance the python script `parser.py` so it can sort the words for all languages based on the respective language dictionary.

Here are the steps to contribute to this repo:

1. Fork this repository
2. Clone the repository to your local

    `git clone https://github.com/<YOUR-USERNAME>/Stop-Words-List.git`
    
3. Create a `.txt` file in `list/` directory and rename it to following format: `[YOUR_LANGUAGE_IN_ENGLISH].txt`. For example:
    - english.txt
    - chinese.txt
    - arabic.txt
  
    > Ignore this step if your language stop words list has already exist in this repo.

4. Put the stop words list in the respective file you have made on step 3/existing stop words list file. **Place only one word in one line**! If you are editing the existing stop words list file, please **DO NOT DELETE/EDIT** anything that already exist. Please ensure that the words you want to add to list have not exist yet in the txt file.
5. Don't forget to put your name in `CONTRIBUTORS.md` and follow the format there.
6. Save the files.
7. Install the dependencies for `parser.py` and run the script. 

    ```
    pip install -r requirements.txt
    python parser.py
    ```
    
    > This script helps you to rearrange the list and sanitize the words.

8. Commit and push to your forked repository.
9. Create the pull request.
10. Congratulations! You have made the priceless contribution.

## Contributing Rules
[`^ back to top ^`](#)

- Place **only one word in one line** in the stop words list txt file.
- To be counted as a contribution, you need to add **at least 10 lines** in your respective language file.
- Please double-check the whole list and ensure the list satisfies these requirements:

    - **No any duplicate words**.
    - All the words in the list, if they are considered as alphabet/LATIN then they must be **lowercase**.
    - Make sure the word list is sorted according to the dictionary.
    - **Each lines** in the list **does not contain any white space/punctuation**.
    
- DO NOT DELETE the previous contributors' names in the CONTRIBUTIORS.md
- When filling the CONTRIBUTORS.md, please make sure the list is arranged in dictionary order based on the language name.
- PRs will be merged if and only if it satisfies all the rules. 


