# ========================================
# Source Dags Factory for Stresstest Tasks
# ========================================
# 
# path_in_mask='/data/DB/AIR/APC/FDW/tsk/*.yaml' \
# dag_prefix='tsk' \
# export PATH=/opt/python_airflow/3.10.10_2.5.2/bin:$PATH

# /usr/bin/env python3 -m ka_air_dfs.dfs \
/opt/python_airflow/3.10.10_2.5.2/bin/ka_air_dfs-dfs \
\
tenant='DB' \
\
path_in_mask='/data/DB/prj/FDW/PWF/wfl/tsk/all/*.yaml' \
dir_out_dag_src='/data/DB/prj/FDW/AIR/dags/tsk/all' \
a_tags='[FDW_TSK]' \
sw_cmd_ix=True \
\
sw_async=False \
sw_debug=False \
sw_run_pid_ts=True \
\
1>dfs_tsk_all.1 2>dfs_tsk_all.2
