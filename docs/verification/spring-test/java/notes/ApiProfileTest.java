package notes;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;
import static org.junit.jupiter.api.Assertions.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;
@SpringBootTest
@AutoConfigureMockMvc
@ActiveProfiles("dev")
class ApiProfileTest {
 @Autowired MockMvc mvc;
 @Autowired CommandLineRunner showBanner;
 @Test void helloAndOpenApi() throws Exception {
  mvc.perform(get("/api/hello")).andExpect(status().isOk()).andExpect(jsonPath("$.message").value("campfire"));
  mvc.perform(get("/v3/api-docs")).andExpect(status().isOk()).andExpect(jsonPath("$.openapi").exists()).andExpect(jsonPath("$.paths['/api/hello']").exists());
 }
 @Test void developmentProfile() throws Exception {
  PrintStream before=System.out;ByteArrayOutputStream captured=new ByteArrayOutputStream();
  try{System.setOut(new PrintStream(captured));showBanner.run();}finally{System.setOut(before);}
  assertTrue(captured.toString().contains("notes.banner=development"));
 }
}
