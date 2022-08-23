# Understanding the Bug Characteristics and Fix Strategies of Federated Learning Systems

This repository consists of three main folders: Dataset_Init, Manual_Labelling and Quantitative_study.

1. **Dataset_Init** folder: The list of initially mined Issues and Pull Rquests(after **Step 1**) for each framework from GitHub is presented in the file `GitHub_init/{frameworkname}/issues_init.csv` and `GitHub_init/{frameworkname}/PRs_init.csv`.

    Total data and data collection process of 6 federated learning frameworks (Data collection until July 20, 2022):
    <table>
        <tr>
            <th rowspan="2">Framework</th>
            <th colspan="5"><div align="center">Total</div></th>
            <th colspan="2"><div align="center">Step1</div></th>
            <th colspan="2"><div align="center">Step2</div></th>
            <th colspan="2"><div align="center">Step3</div></th>
        </tr>
        <tr>
            <td><div align="right">LOC</div></td>
            <td><div align="right">Forks</div></td>
            <td><div align="right">Stars</div></td>
            <td><div align="right">Issues</div></td>
            <td><div align="right">PRs</div></td>
            <td><div align="right">Issues</div></td>
            <td><div align="right">PRs</div></td>
            <td><div align="right">Issues</div></td>
            <td><div align="right">PRs</div></td>
            <td><div align="right">Issues</div></td>
            <td><div align="right">PRs</div></td>
        </tr>
        <tr>
            <td>
                <div align="center">PySyft</div>
                <div align="center">FATE</div>
                <div align="center">TFF</div>
                <div align="center">Flower</div>
                <div align="center">Fedlearner</div>
                <div align="center">PaddleFL</div>
            </td>
            <td>
                <div align="right">3.8m</div>
                <div align="right">497.3k</div>
                <div align="right">206.5k</div>
                <div align="right">49.1k</div>
                <div align="right">209.8k</div>
                <div align="right">87.0k</div>
            </td>
            <td>
                <div align="right">1,833</div>
                <div align="right">1,310</div>
                <div align="right">473</div>
                <div align="right">293</div>
                <div align="right">166</div>
                <div align="right">102</div>
            </td>
            <td>
                <div align="right">8,218</div>
                <div align="right">4,371</div>
                <div align="right">1,901</div>
                <div align="right">1,136</div>
                <div align="right">783</div>
                <div align="right">393</div>
            </td>
            <td>
                <div align="right">3,062</div>
                <div align="right">834</div>
                <div align="right">242</div>
                <div align="right">118</div>
                <div align="right">20</div>
                <div align="right">65</div>
            </td>
            <td>
                <div align="right">3,491</div>
                <div align="right">2,800</div>
                <div align="right">2,630</div>
                <div align="right">894</div>
                <div align="right">944</div>
                <div align="right">153</div>
            </td>
            <td>
                <div align="right">439</div>
                <div align="right">271</div>
                <div align="right">163</div>
                <div align="right">35</div>
                <div align="right">6</div>
                <div align="right">24</div>
            </td>
            <td>
                <div align="right">649</div>
                <div align="right">163</div>
                <div align="right">173</div>
                <div align="right">36</div>
                <div align="right">35</div>
                <div align="right">14</div>
            </td>
            <td>
                <div align="right">270</div>
                <div align="right">224</div>
                <div align="right">68</div>
                <div align="right">22</div>
                <div align="right">4</div>
                <div align="right">11</div>
            </td>
            <td>
                <div align="right">386</div>
                <div align="right">129</div>
                <div align="right">96</div>
                <div align="right">13</div>
                <div align="right">29</div>
                <div align="right">11</div>
            </td>
            <td>
                <div align="right">80</div>
                <div align="right">79</div>
                <div align="right">21</div>
                <div align="right">8</div>
                <div align="right">2</div>
                <div align="right">2</div>
            </td>
            <td>
                <div align="right">49</div>
                <div align="right">46</div>
                <div align="right">26</div>
                <div align="right">5</div>
                <div align="right">11</div>
                <div align="right">6</div>
            </td>
        </tr>
        <tr>
            <td><div align="center">Sum</div></td>
            <td><div align="right">4.8m</div></td>
            <td><div align="right">4,177</div></td>
            <td><div align="right">16,802</div></td>
            <td><div align="right">4,341</div></td>
            <td><div align="right">10,912</div></td>
            <td><div align="right">938</div></td>
            <td><div align="right">1,070</div></td>
            <td><div align="right">599</div></td>
            <td><div align="right">664</div></td>
            <td><div align="right">192</div></td>
            <td><div align="right">143</div></td>
    </table>

    The list of StackOverflow bugs based on tag and keywords is presented in the file [Dataset_init/SO_init/SO_init.csv](Dataset_init/SO_init/SO_init.csv).
2. **Manual_Labelling** folder: In this folder, we have placed all the files associated with our manual labelled result. For the bugs, we further annotate `Symptom`, `Source of Bug`, `Bug Type` and `Root cause`.

    Noted that bugs in `Documentation` and `Others` are excluded from root cause analysis because of their irrelevance to the core FL functions, and bugs from Pull Requests (PRs) are excluded from `Symptom` because in our observations, most PRs are submitted by framework developers or maintainers with limited information.
3. **Quantitative_Study** folder: In this folder, we have placed the source data from Quantitative Study in Section 7.1. In the lifecycle file from Github, we annotate the creation time, closing time and lifecycle.
   In the lifecycle file from StackOverflow, we annotate the creation time, last active time and lifecycle.

    In files of patch size, we annotate the number of added lines, deleted lines, the total number of lines, and changed files.

For the fix strategy, since some instances do not have a clear fix strategy, we summarize some common fix strategies and analyze which root cause can be fixed by them.

**The relationship table between symptom and root cause**:  

<div align=center>
    <img src="Relationship_between_symptom_and_root_cause.svg" width="650">
</div>

This relationship figure presents the number of the top 10 root causes for bugs with each symptom. 
Except for *Incorrect Deployment*, *Crash* is the most common symptom for all these root causes. 
We also find that all bugs exhibiting the symptom of *Incorrect Deployment* are produced by *Incorrect Deployment*. 
On the other hand, 83.33\% of bugs exhibiting symptom *Connection Refused* are produced by *Interaction Issues*, which indicates that developers can be suggested to check the implementation of interaction between different parties when a *Connection Refused* bug occurs.

**The relationship table between fix strategy and root cause**:  

<div align=center>
    <img src="Relationship_between_fix_and_root_cause.svg" width="650">
</div>

