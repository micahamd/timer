[33mcommit ecc79e144b1e9438cfeefcf25479f492703c1f86[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmaster[m[33m, [m[1;31morigin/master[m[33m)[m
Author: Micah A <micah.amd.eab@hotmail.com>
Date:   Tue Mar 19 23:28:45 2024 +1200

    timer v1

[1mdiff --git a/.idea/.gitignore b/.idea/.gitignore[m
[1mnew file mode 100644[m
[1mindex 0000000..eaf91e2[m
[1m--- /dev/null[m
[1m+++ b/.idea/.gitignore[m
[36m@@ -0,0 +1,3 @@[m
[32m+[m[32m# Default ignored files[m[41m[m
[32m+[m[32m/shelf/[m[41m[m
[32m+[m[32m/workspace.xml[m[41m[m
[1mdiff --git a/.idea/inspectionProfiles/profiles_settings.xml b/.idea/inspectionProfiles/profiles_settings.xml[m
[1mnew file mode 100644[m
[1mindex 0000000..105ce2d[m
[1m--- /dev/null[m
[1m+++ b/.idea/inspectionProfiles/profiles_settings.xml[m
[36m@@ -0,0 +1,6 @@[m
[32m+[m[32m<component name="InspectionProjectProfileManager">[m
[32m+[m[32m  <settings>[m
[32m+[m[32m    <option name="USE_PROJECT_PROFILE" value="false" />[m
[32m+[m[32m    <version value="1.0" />[m
[32m+[m[32m  </settings>[m
[32m+[m[32m</component>[m
\ No newline at end of file[m
[1mdiff --git a/.idea/misc.xml b/.idea/misc.xml[m
[1mnew file mode 100644[m
[1mindex 0000000..a17385c[m
[1m--- /dev/null[m
[1m+++ b/.idea/misc.xml[m
[36m@@ -0,0 +1,7 @@[m
[32m+[m[32m<?xml version="1.0" encoding="UTF-8"?>[m[41m[m
[32m+[m[32m<project version="4">[m[41m[m
[32m+[m[32m  <component name="Black">[m[41m[m
[32m+[m[32m    <option name="sdkName" value="Python 3.12 (timer)" />[m[41m[m
[32m+[m[32m  </component>[m[41m[m
[32m+[m[32m  <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.12 (timer)" project-jdk-type="Python SDK" />[m[41m[m
[32m+[m[32m</project>[m
\ No newline at end of file[m
[1mdiff --git a/.idea/modules.xml b/.idea/modules.xml[m
[1mnew file mode 100644[m
[1mindex 0000000..2507d08[m
[1m--- /dev/null[m
[1m+++ b/.idea/modules.xml[m
[36m@@ -0,0 +1,8 @@[m
[32m+[m[32m<?xml version="1.0" encoding="UTF-8"?>[m[41m[m
[32m+[m[32m<project version="4">[m[41m[m
[32m+[m[32m  <component name="ProjectModuleManager">[m[41m[m
[32m+[m[32m    <modules>[m[41m[m
[32m+[m[32m      <module fileurl="file://$PROJECT_DIR$/.idea/timer.iml" filepath="$PROJECT_DIR$/.idea/timer.iml" />[m[41m[m
[32m+[m[32m    </modules>[m[41m[m
[32m+[m[32m  </component>[m[41m[m
[32m+[m[32m</project>[m
\ No newline at end of file[m
[1mdiff --git a/.idea/timer.iml b/.idea/timer.iml[m
[1mnew file mode 100644[m
[1mindex 0000000..f246f2c[m
[1m--- /dev/null[m
[1m+++ b/.idea/timer.iml[m
[36m@@ -0,0 +1,10 @@[m
[32m+[m[32m<?xml version="1.0" encoding="UTF-8"?>[m[41m[m
[32m+[m[32m<module type="PYTHON_MODULE" version="4">[m[41m[m
[32m+[m[32m  <component name="NewModuleRootManager">[m[41m[m
[32m+[m[32m    <content url="file://$MODULE_DIR$">[m[41m[m
[32m+[m[32m      <excludeFolder url="file://$MODULE_DIR$/.venv" />[m[41m[m
[32m+[m[32m    </content>[m[41m[m
[32m+[m[32m    <orderEntry type="inheritedJdk" />[m[41m[m
[32m+[m[32m    <orderEntry type="sourceFolder" forTests="false" />[m[41m[m
[32m+[m[32m  </component>[m[41m[m
[32m+[m[32m</module>[m
\ No newline at end of file[m
[1mdiff --git a/.vscode/launch.json b/.vscode/launch.json[m
[1mnew file mode 100644[m
[1mindex 0000000..8b27833[m
[1m--- /dev/null[m
[1m+++ b/.vscode/launch.json[m
[36m@@ -0,0 +1,15 @@[m
[32m+[m[32m{[m[41m[m
[32m+[m[32m    // Use IntelliSense to learn about possible attributes.[m[41m[m
[32m+[m[32m    // Hover to view descriptions of existing attributes.[m[41m[m
[32m+[m[32m    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387[m[41m[m
[32m+[m[32m    "version": "0.2.0",[m[41m[m
[32m+[m[32m    "configurations": [[m[41m[m
[32m+[m[32m        {[m[41m[m
[32m+[m[32m            "name": "Python Debugger: Current File",[m[41m[m
[32m+[m[32m            "type": "debugpy",[m[41m[m
[32m+[m[32m            "request": "launch",[m[41m[m
[32m+[m[32m            "program": "${file}",[m[41m[m
[32m+[m[32m            "console": "integratedTerminal"[m[41m[m
[32m+[m[32m        }[m[41m[m
[32m+[m[32m    ][m[41m[m
[32m+[m[32m}[m
\ No newline at end of file[m
[1mdiff --git a/__pycache__/activity_main.cpython-312.pyc b/__pycache__/activity_main.cpython-312.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..e4c1608[m
Binary files /dev/null and b/__pycache__/activity_main.cpython-312.pyc differ
[1mdiff --git a/__pycache__/data_storage.cpython-312.pyc b/__pycache__/data_storage.cpython-312.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..58eb1b1[m
Binary files /dev/null and b/__pycache__/data_storage.cpython-312.pyc differ
[1mdiff --git a/__pycache__/visualization.cpython-312.pyc b/__pycache__/visualization.cpython-312.pyc[m
[1mnew file mode 100644[m
[1mindex 0000000..046113e[m
Binary files /dev/null and b/__pycache__/visualization.cpython-312.pyc differ
[1mdiff --git a/activities.json b/activities.json[m
[1mnew file mode 100644[m
[1mindex 0000000..84a41e1[m
[1m--- /dev/null[m
[1m+++ b/activities.json[m
[36m@@ -0,0 +1 @@[m
[32m+[m[32m{"READ": "#0000FF", "STUDY": "#FFFFFF"}[m
\ No newline at end of file[m
[1mdiff --git a/activities.txt b/activities.txt[m
[1mnew file mode 100644[m
[1mindex 0000000..0ff04c2[m
[1m--- /dev/null[m
[1m+++ b/activities.txt[m
[36m@@ -0,0 +1,3 @@[m
[32m+[m[32mREAD[m[41m[m
[32m+[m[32mSTUDY[m[41m[m
[32m+[m[32mAdmin[m[41m[m
[1mdiff --git a/activity_log.json b/activity_log.json[m
[1mnew file mode 100644[m
[1mindex 0000000..710dbd4[m
[1m--- /dev/null[m
[1m+++ b/activity_log.json[m
[36m@@ -0,0 +1,445 @@[m
[32m+[m[32m{[m[41m[m
[32m+[m[32m    "activities": {[m[41m[m
[32m+[m[32m        "Study": [[m[41m[m
[32m+[m[32m            {[m[41m[m
[32m+[m[32m                "start": "2024-03-02 17:21:34",[m[41m[m
[32m+[m[32m                "end": "2024-03-02 17:21:34"[m[41m[m
[32m+[m[32m            },[m[41m[m
[32m+[m[32m            {[m[41m[m
[32m+[m[32m                "start": "2024-03-02 17:21:35",[m[41m[m
[32m+[m[32m                "end": "2024-03-02 17:21:35"[m[41m[m
[32m+[m[32m            },[m[41m[m
[32m+[m[32m            {[m[41m[m
[32m+[m[32m                "start": "2024-03-02 17:21:36",[m[41m[m
[32m+[m[32m                "end": "2024-03-02 17:21:36"[m[41m[m
[32m+[m[32m            },[m[41m[m
[32m+[m[32m            {[m[41m[m
[32m+[m[32m                "start": "2024-03-02 17:21:37",[m[41m[m
[32m+[m[32m                "end": "2024-03-02 17:21:38"[m[41m[m
[32m+[m[32m            },[m[41m[m
[32m+[m[32m            {[m[41m[m
[32m+[m[32m                "start": "2024-03-02 17:30:58",[m[41m[m
[32m+[m[32m                "end": "2024-03-02 17:31:03"[m[41m[m
[32m+[m[32m            },[m[41m[m
[32m+[m[32m            {[m[41m[m
[32m+[m[32m                "start": "2024-03-02 17:31:05",[m[41m[m
[32m+[m[32m                "end": "2024-03-02 17:31:05"[m[41m[m
[32m+[m[32m            },[m[41m[m
[32m+[m[32m            {[m[41m[m
[32m+[m[32m                "start": "2024-03-02 18:20:42",[m[41m[m
[32m+[m[32m                "end": "2024-03-02 18:20:43",[m[41m[m
[32m+[m[32m                "duration": 1.268481[m[41m[m
[32m+[m[32m            },[m[41m[m
[32m+[m[32m            {[m[41m[m
[32m+[m[32m                "start": "2024-03-02 18:20:43",[m[41m[m
[32m+[m[32m                "end": "2024-03-02 18:20:44",[m[41m[m
[32m+[m[32m                "duration": 0.810777[m[41m[m
[32m+[m[32m            },[m[41m[m
[32m+[m[32m            {[m[41m[m
[32m+[m[32m                "start": "2024-03-19 16:03:52",[m[41m[m
[32m+[m[32m                "end": "2024-03-19 16:03:53",[m[41m[m
[32m+[m[32m                "duration": 0.853458[m[41m