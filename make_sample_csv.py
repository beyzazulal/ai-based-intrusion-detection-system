import pandas as pd

source_csv = r"D:\bit.pro\Friday-WorkingHours-Morning.pcap_ISCX.csv"
out_csv = r"D:\bit.pro\sample_full_row.csv"

df = pd.read_csv(source_csv, low_memory=False)
df.columns = df.columns.str.strip()

# Label sütununu çıkar, sadece feature'lar kalsın
df = df.drop(columns=["Label"])

# İlk satırı kaydet
df.iloc[[0]].to_csv(out_csv, index=False)

print("Oluşturuldu:", out_csv)
print("Kolon sayısı:", len(df.columns))