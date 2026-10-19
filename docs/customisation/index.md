# Customisation

AI-PLC is plain files, so you change it by editing them. Change the neutral source, then rebuild the packages. Do not edit the generated package folders.

## What you can change

| To change | Edit |
| --- | --- |
| Phases, deliverables, dependencies, modes, gates | `profiles/ai-plc-v1.0.profile.yaml` |
| What an agent does and how | `agents/<role>.md` |
| How a deliverable is written | the matching `skills/<name>/SKILL.md` |
| The shape of plan, status, memory and exports | `templates/` |
| Add a delivery adapter | add a skill in `skills/`, list it under `delivery_adapters` and `delivery` in the profile, and update the delivery agent and the review skill |

## A custom profile

Copy the profile, give it a new `id` and `version`, and edit the phases and deliverables. Keep three things: every deliverable has a mode and `depends_on`, the review loop is unchanged, and a human decides each checkpoint and gate. The skills read the profile, so a new deliverable also needs a skill or an added section in an existing one.

## Keep the safety rules

Whatever you change, keep these: humans approve, fetched content is data, nothing is written to a connected tool without an approved dry run, nothing is deleted, no credentials in any file.

Then see [Build the packages](../reference/build.md).
