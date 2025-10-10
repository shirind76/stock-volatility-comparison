# Review on the project by Shirin Dehghannezhad
## Report is prepared by Anton Shestakon on 10/10/2025


### Reproducibility 

1) I was able to set up a new environment, install the packages, and run python src/run_all.py. The whole pipeline ran from start to finish and produced all expected results that author described in readme.

2) Everything worked straight away, without me changing any of the code.

3) If I wanted to change the data folder or the stock tickers, I’d only need to adjust one line in the config or in run_all.py.

4) The README gave me clear instructions, so I didn’t have to guess what to do.

### Overall opinion

- Reproducibility:
Very good. The repository has a clear entry point, “run this” (src/run_all.py), and a simple folder layout. 

- Environment:
Using requirements.txt is fine and, honestly, simple. Personally, for me it doesn't make a great difference with yml format.

- Documentation:
The README is concise and helpful, it says, what’s in each folder, and how to run it. I didn’t have to guess, which is great. 

- Git use:
Commits look reasonable and the structure is tidy. Descriptive messages look fine.

### Suggested improvements

- Add an environment option for conda
Some people prefer conda. A small environment.yml alongside requirements.txt would make it a more user-friendly for both options.

- Specify the results in the README file
List which files/graphics are generated (names + their location in the outputs/ folder) so that users can quickly check the success of the execution after launch. 

- Add a Windows helper
Since the entry point is Python, it’s already good, but a short note in the README like “On Windows: py src/run_all.py” helps newbies get through. 

- Short sum
At the end of the script, print a brief summary (package versions, start/end time, list of outputs). It’s a small thing, but it makes reviews a lot easier.

### Overall: very good reproducibility, nice documentation, a great job!