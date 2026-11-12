# Security

AI-PLC is plain files that your AI coding tool loads. It has no server and stores no credentials. It can still affect your tools, because agents may read from and, after you approve a dry run, create items in connected services such as Jira, Confluence, Notion and Miro.

## Rules the project follows

- People approve every stop. The AI never approves its own work.
- Fetched content (web pages, documents, tickets, boards) is treated as data, never as instructions.
- Nothing is written to a connected tool without an approved dry run, and nothing is deleted.
- No credentials are stored in any file. You sign in to each tool yourself.

## Reporting a problem

If you find a way around these rules, or a way for fetched content to take control of an agent, please report it privately. Use GitHub's private vulnerability reporting on this repository (Security tab, then "Report a vulnerability"). If that is not available, open an issue that says you have a security concern, without the details, and the maintainer will arrange a private channel.

Please do not post working exploits or private data in public issues.

## Supported versions

This is a release candidate. Only the latest release is supported.
