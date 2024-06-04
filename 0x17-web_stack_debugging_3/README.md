# 0x17. Web stack debugging #3

**Background Context**

During debugging, logging may not always provide sufficient insight. This might be due to unexpected software behavior or logs lacking essential details. In such scenarios, delving into the stack trace becomes crucial. Mastering this skill is a valuable asset for Holberton students embarking on their software development journeys.

WordPress, a widely-used platform for blogs, portfolios, e-commerce ventures, and company websites, powers a significant portion of the web (approximately 26%). As a developer, encountering WordPress projects is highly likely throughout your career.

This exercise focuses on debugging a WordPress website running on the LAMP stack (Linux, Apache, MySQL, and PHP), a prevalent web development environment.

**Requirements**

- **General:**
    - Ubuntu 14.04 LTS as the development environment.
    - All files must conclude with a new line character (carriage return).
    - A mandatory `README.md` file at the project's root directory.
    - Error-free Puppet manifests, passing `puppet-lint` v2.1.1 validation.
    - Execution of Puppet manifests without errors.
    - First line of each Puppet manifest serving as a comment explaining its purpose.
    - File extensions for Puppet manifests ending in `.pp`.
    - Puppet v3.4 used for file verification.
- **Installation:**
    ```bash
    sudo apt-get install -y ruby
    sudo gem install puppet-lint -v 2.1.1
    ```

**Tasks**

**0. Strace: Your Debugging Ally (Mandatory)**

Leveraging `strace`, uncover the cause behind the 500 error returned by Apache. Upon identifying the issue, implement an automated fix using Puppet instead of a manual Bash solution.

**Hint:**

- `strace` can attach to running processes.
- Utilize `tmux` to run `strace` in one window and `curl` (or another HTTP client) in another for interaction and observation.

**Requirements:**

- `0-strace_is_your_friend.pp` must contain the necessary Puppet code to automate the fix.
- Flexibility in choosing the appropriate Puppet resource type to address the discovered issue.
