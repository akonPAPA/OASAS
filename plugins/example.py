"""Example OASAS plugin. Copy this file to build your own drop-in commands
You can fully manipulate with this shit so IDK maby , have my number? so call me babe, Yeah I just met u and this is crazy here 
is my number so call me maybe

Any .py file in plugins/ exposing register(api) is auto-loaded at shell start
"""


def register(api):
    def whoami(session, args):
        api.console.print(
            f"provider: {session.provider_label()}  ·  "
            f"workspace: {session.workspace_label()}  ·  "
            f"scope: {session.scope_label()}"
        )

    def note_finding(session, args):
        # demo: quickly stash a manual note as a finding
        if not session.workspace or not args:
            api.console.print("usage: quicknote <text...>  (needs an open workspace)")
            return
        session.workspace.add_note(" ".join(args))
        api.console.print("[+] note saved")

    api.add_command("whoami", whoami, "example: print the active session context")
    api.add_command("quicknote", note_finding, "example: quick-save an engagement note")
