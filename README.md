# Pet Finder
This is the documentation for the Pet Finder Django application. 

## Installation
The latest Docker image is available on Docker Hub at `redwancse/pets-finder:latest`.

## Run the container
Use this command to run the latest release:
```shell
docker run -dp 0.0.0.0:8000:8000 redwancse/pets-finder:latest
```

## Merging Changes into Develop Branch (Team SkyWalkers):
As part of our collaborative development process, the "develop" branch is open for your feature branches to be merged. Please follow these guidelines:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/redwan-cse/pets-finder.git
   cd pets-finder
   ```

2. **Create a Feature Branch:**
   ```bash
   git checkout -b feature/your-feature-name develop
   ```

3. **Make Changes:**
   - Make the necessary changes to your code.
   ```bash
   git status
   ```

4. **Commit Changes:**
   - Use `git add -u` when you only want to stage modifications and deletions to tracked files
   - Use `git add .` when you want to stage all changes, including new, modified, and deleted files.
   - You might need to use both commands or `git add -A` to stage all changes.
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

5. **Push Feature Branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request:**
   - Go to the repository on [platform] and create a pull request targeting "develop."
   ```bash
   git request-pull -p <base> <head>
   ```
   Replace `<base>` with the name of the branch you want to merge into (e.g., "develop") and `<head>` with the name of your feature branch (e.g., "feature/your-feature-name").

   For example:
   ```bash
   git request-pull -p develop feature/your-feature-name
   ```

7. **Review and Merge:**
   - Team members, please review and test pull requests promptly.
   - Feel free to merge your own pull requests after receiving approval, or request reviews from others.

8. **Keep "develop" Updated:**
   - Regularly pull changes from "develop" into your feature branch to avoid conflicts.

   ```bash
   git pull origin develop
   ```
9. **Test the beta images:**
   Use this command to run the devlop branch image:
   ```shell
   docker run -dp 0.0.0.0:8000:8000 redwancse/pets-finder:beta
   ```
