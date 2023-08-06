# ========================================
# Source Dags Factory for Stresstest Tasks
# ========================================
# 
# path_in_mask='/data/DB/AIR/APC/FDW/tsk/*.yaml' \
# dag_prefix='tsk' \

# /usr/bin/env python3 -m ka_air_dfs.dfs \
/opt/airflow/dev1/latest/python/bin/ka_air_dfs-dfs \
\
tenant='DB' \
\
path_in_mask='/data/DB/prj/FDW/PWF/wfl/tsk/mon/*.yaml' \
dir_out_dag_src='/data/DB/prj/FDW/AIR/dags/tsk/mon' \
a_tags='[FDW_TSK]' \
sw_cmd_ix=True \
\
sw_async=False \
sw_debug=False \
sw_run_pid_ts=True \
\
1>dfs_tsk_mon.1 2>dfs_tsk_mon.2
