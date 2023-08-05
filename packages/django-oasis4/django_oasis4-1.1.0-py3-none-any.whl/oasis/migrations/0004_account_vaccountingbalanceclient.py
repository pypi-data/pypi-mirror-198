# Generated by Django 4.1.5 on 2023-01-27 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oasis', '0003_oasiscompany_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('companyid', models.IntegerField(primary_key=True, serialize=False)),
                ('plan', models.IntegerField()),
                ('accountid', models.BigIntegerField()),
                ('accountname', models.CharField(blank=True, max_length=100, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('parent', models.BigIntegerField(blank=True, null=True)),
                ('nature', models.CharField(blank=True, max_length=1, null=True)),
                ('impute', models.BooleanField(blank=True, null=True)),
                ('client', models.BooleanField(blank=True, null=True)),
                ('costcenter', models.BooleanField(blank=True, null=True)),
                ('business', models.BooleanField(blank=True, null=True)),
                ('project', models.BooleanField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=1, null=True)),
                ('retention', models.BooleanField(blank=True, null=True)),
                ('percentageretention', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('reference', models.BooleanField(blank=True, null=True)),
                ('adjustment', models.BooleanField(blank=True, null=True)),
                ('adjustmentaccount1', models.BigIntegerField(blank=True, null=True)),
                ('adjustmentaccount2', models.BigIntegerField(blank=True, null=True)),
                ('repetitive', models.BooleanField(blank=True, null=True)),
                ('repetitiveaccount1', models.BigIntegerField(blank=True, null=True)),
                ('repetitiveaccount2', models.BigIntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('utility', models.BooleanField(blank=True, null=True)),
                ('module', models.CharField(blank=True, max_length=1, null=True)),
                ('currency', models.CharField(blank=True, max_length=1, null=True)),
                ('currencyid', models.IntegerField(blank=True, null=True)),
                ('baseretention', models.BooleanField(blank=True, null=True)),
                ('percentagebudget', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('oldcode', models.CharField(blank=True, max_length=20, null=True)),
                ('budget', models.BooleanField(blank=True, null=True)),
                ('budgetcontrol', models.BooleanField(blank=True, null=True)),
                ('order', models.BigIntegerField(blank=True, null=True)),
                ('alternatecode', models.CharField(blank=True, max_length=20, null=True)),
                ('expenseobjectid', models.IntegerField(blank=True, null=True)),
                ('entryid', models.IntegerField(blank=True, null=True)),
                ('ordinary', models.CharField(blank=True, max_length=1, null=True)),
                ('accountname1', models.CharField(blank=True, max_length=100, null=True)),
                ('abc', models.CharField(blank=True, max_length=1, null=True)),
                ('bookid', models.IntegerField(blank=True, null=True)),
                ('updated', models.DateField(blank=True, null=True)),
                ('product', models.BooleanField(blank=True, null=True)),
                ('codeid', models.CharField(blank=True, max_length=3, null=True)),
                ('tax', models.CharField(blank=True, max_length=1, null=True)),
                ('businessid', models.IntegerField(blank=True, null=True)),
                ('updatedby', models.IntegerField(blank=True, null=True)),
                ('taxtypeid', models.IntegerField(blank=True, null=True)),
                ('quantitytype', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VAccountingBalanceClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField(db_column='companyid')),
                ('client_id', models.BigIntegerField(db_column='clientid')),
                ('year', models.IntegerField()),
                ('period', models.IntegerField()),
                ('plan', models.IntegerField()),
                ('account_id', models.BigIntegerField(db_column='accountid')),
                ('book_id', models.IntegerField(db_column='bookid')),
                ('debit', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('credit', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('debit_base', models.DecimalField(blank=True, db_column='debitbase', decimal_places=4, max_digits=19, null=True)),
                ('credit_base', models.DecimalField(blank=True, db_column='creditbase', decimal_places=4, max_digits=19, null=True)),
                ('balance_base', models.DecimalField(blank=True, db_column='balancebase', decimal_places=4, max_digits=19, null=True)),
            ],
            options={
                'db_table': 'v_AccountingBalanceClient',
                'managed': False,
            },
        ),
    ]
