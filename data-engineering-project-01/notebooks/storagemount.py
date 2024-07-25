# Databricks notebook source
# MAGIC %md
# MAGIC # Mount Points
# MAGIC This script will mount the bronze, silver and gold mount points.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Overview
# MAGIC
# MAGIC | test | Information |
# MAGIC |------|-------------|
# MAGIC |Created By | Todd Wilson ([todd-wilson@outlook.com](mailto:todd-wilson@outlook.com)) |
# MAGIC | Portfolio | https://todd-wilson.github.io |

# COMMAND ----------

# MAGIC %md
# MAGIC ## History
# MAGIC | Date | Developer | Changes |
# MAGIC |------|-----------|---------|
# MAGIC | 07-24-2024 | Todd Wilson | Notebook created to mount bronze, silver and gold layers. |

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount Bronze

# COMMAND ----------

configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

container_name = "bronze"
storage_account_name = "portfoliodl24601"
mount_point = f"/mnt/{container_name}"
folder_name = "SalesLT"

dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = mount_point,
  extra_configs = configs
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount Silver

# COMMAND ----------

container_name = "silver"
storage_account_name = "portfoliodl24601"
mount_point = f"/mnt/{container_name}"
#folder_name = "SalesLT"

dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = mount_point,
  extra_configs = configs
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount Gold

# COMMAND ----------

container_name = "gold"
storage_account_name = "portfoliodl24601"
mount_point = f"/mnt/{container_name}"
#folder_name = "SalesLT"

dbutils.fs.mount(
  source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
  mount_point = mount_point,
  extra_configs = configs
)
