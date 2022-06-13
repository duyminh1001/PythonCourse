vandic = {
	"hot": "nóng",
	"beach": "biển",
	"miss": "nhớ, bỏ lở ",
	"apple": "quả táo"
}
#print(vandic.keys())
vandic["children"] = "trẻ em"
#print(vandic)
x="hot" in vandic
y= "van" in vandic
print(x ,"neu co hot co nghia la ", vandic["hot"])
print (y , "khong co tu")